from src.EcmsApi.queries import SQLQuery
from src.EcmsApi.HR import HRTEMP

table = SQLQuery(HRTEMP)
query = table.select()

query.filters(employeeno=12345, companyno=50, divisionno=2)
query.columns(['CompanyNo', 'DivisionNo', 'EmployeeNo', 'City'])
query.order(by='City')
query.head()

response = query.query()
