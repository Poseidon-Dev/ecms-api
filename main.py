from src.conn import Conn
from src.models import TableSchema
from src.hr import Property, Master

hr = Property()

hr.columns(['HRTEMPID', 'propertyno', 'description', 'controlno'])

hr.filters(propertyno=9,)
data = hr.to_df()
print(data)



