from os import name
from src.conn import Conn
import pandas as pd
import pyodbc

class QueryValidator:

    def update_validation(self, command):
        if 'UPDATE' in command and 'SET' not in command: 
            raise SyntaxError('Update syntax incorrect, missing "SET"')
        else:
            pass

    def select_validation(self, command):
        if 'SELECT' in command and 'AND' in command:
            raise SyntaxError('SELECT syntax incorrect, missing "WHERE" clause')
        else:
            pass

    def delete_validation(self, command):
        if 'DELETE' in command and 'WHERE' not in command:
            raise SyntaxError('DELETE syntax incorrect, missing "WHERE" clause, need to be more specific')
        else:
            pass

    def validator(self, command):
        self.update_validation(command)
        self.select_validation(command)
        self.delete_validation(command)

class TableSchema(Conn):

    namespace = Conn.host
    ALLOWABLE_OPERATORS = ['=', '<', '>', '<>']
    ALLOWABLE_METHODS = ['DELETE', 'SELECT', 'UPDATE']
    TABLE_NAME = ''


    def __init__(self):
        self.command = f'METHOD COLS FROM {self.namespace}.{self.table} '
        super().__init__()


    @property
    def table(self):
        return self.TABLE_NAME


    @property
    def id (self):
        return f'{self.table}ID'


    @property
    def cols(self):
        return [{k:v} for k,v in self.__class__.__dict__.items() if '__' not in k]


    @property
    def column_names(self):
        return [col for cols in self.cols for col,_ in cols.items()]

    
    def all(self):
        command = f'SELECT * FROM {self.namespace}.{self.table} '
        return self.execute(command)

    
    def filter(self, column:str, value, op: str = "="):
        if column.upper() in self.column_names:
            if op in self.ALLOWABLE_OPERATORS:
                if 'WHERE' not in self.command:
                    self.command += 'WHERE '
                else:
                    self.command += 'AND '
                self.command += f"{column.upper()} {op} '{value}' "
                return self
            else:
                raise ValueError(f'"{op}" is not an allowable operator')
        else:
            raise ValueError(f'{column.upper()} is not a column in {self.table}')


    def filters(self, **kwargs):
        for column, value in kwargs.items():
            self.filter(column, value)
        return self


    def order(self, by: str = '', order: str = 'ASC'):
        if not by:
            by = self.id
        self.command += f'ORDER BY {by} {order} '
        return self

    
    def limit(self, amount=1):
        self.command += f'LIMIT {amount} '

    
    def columns(self, columns:list):
        for col in columns:
            if col.upper() not in self.column_names:
                raise ValueError(f'{col} is not a column in {self.table}')
        self.columns = columns
        columns = ', '.join(columns)
        self.command = self.command.replace('COLS', columns)

    
    def head(self, amount=10):
        if 'LIMIT' not in self.command:
            self.limit(amount)


    def method(self, method):
        self.command = self.command.replace('METHOD', method)
        if method in ['DELETE', 'UPDATE']:
            self.command = self.command.replace('* ', '')
        return self


    def query(self, method:str='SELECT'):
        self.finalize_command(method)
        return self.execute(self.command)


    def to_df(self, method:str='SELECT'):
        self.finalize_command(method)
        conn = pyodbc.connect(Conn.connection_string)
        return pd.read_sql(self.command, conn)

    
    def to_excel(self, method:str='SELECT', name='dumps\export.xlsx', index=False, header=True):
        self.to_df().to_excel(name, index=index, header=header)

       
    def finalize_command(self, method):
        self.method(method.upper())
        if 'COLS' in self.command:
            self.command = self.command.replace('COLS', '*')
        QueryValidator().validator(self.command)
        return self


    def __str__(self):
        return self.command

