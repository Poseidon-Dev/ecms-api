from src.EcmsApi.queries import SQLQuery
from src.EcmsApi.HR import HRTEMP

q = SQLQuery(HRTEMP).select()

print(q.filters(employeeno=12799).to_excel('somenewfilename'))

