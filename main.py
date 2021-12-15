from src import HR

hr = HR.Master()
data = hr.filter('employeeno', 18000, '>').to_excel()
