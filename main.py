from src.conn import Conn
from src.models import TableSchema
from src.hr.models import HRTEMP

hr = HRTEMP()
hr.filters(employeeno=12799)
hr.columns(['companyno', 'employeeno', 'companyno', 'deptno'])
data = hr.to_df()
print(data)



