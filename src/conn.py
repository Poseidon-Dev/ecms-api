import os
import pyodbc

class Conn:

    host = os.getenv('ECMS_HOST')
    uid = os.getenv('ECMS_UID')
    pwd = os.getenv('ECMS_PWD')
    connection_string = f'DSN={host}; UID={uid}; PWD={pwd}'


    def select(self):
        pass

    def update(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass
    
    def execute(self, command):
        try:
            conn = pyodbc.connect(self.connection_string)
            cur = conn.cursor()
            cur.execute(command)
            resp = cur.fetchall()
            return list(resp)
        except Exception as e:
            print(e)



