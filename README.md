# ECMS-API

ECMS-API is a query wrapper that allows for querying the AS400 directly

## Authors

**[Johnny Whitworth (@Poseidon-dev)](https://github.com/poseidon-dev)** 

## How to use Examples

Select
```python
table = SQLQuery(HRTEMP)
query = table.select()

query.filter(employeeno=12345, companyno=50, divisionno=2)
query.columns(['CompanyNo', 'DivisionNo', 'EmployeeNo', 'Department'])

response = query.query()
```

The select method also allows for queried data to be saved as an excel doc using .to_excel() rather than .query()


Update
```python
table = SQLQuery(HRTEMP)
query = table.update()

query.sets(departmentno=41, companyno=50)
query.filter(employeeno=12345)
query.query()
```

## Support

If you need some help for something, please reach out to me directly or submit an issue and I'll get to it as soon as I can

## Site

https://poseidon-dev.github.io/ecms-api/
