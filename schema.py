import pyodbc #python open database connectvity
from Emp import Emp_Details
# declare Global variables used connect to DB
server = 'HCL-02-123\SQLEXPRESS'
database = 'Emp123'
username = 'Rajyalakshmi'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
"""class classalredyexist(Exception):
    print("This class is alredy exits")"""
class Employee:
    def create_employee_table(self):
        query=cursor.execute('''
        create table Employee_details(
        Empname varchar(50),
        empproject varchar(50),
        empsalary int)
        ''')
        print(query)
        query=cursor.execute('''
        INSERT INTO Employee_details(Empname,empproject,empsalary)
        ''')
        cursor.commit()
        query=cursor.execute('''
        upload_employee_details()
        ''')
        cursor.commit()

    def upload_employee_details(self,employee,employeeproject,employeesalary):
        print("employee=",self.employee)
        print("employeeproject=",self.employeeproject)
        print("employeesalary=",self.employeesalary)

ob=Employee()
ob.create_employee_table()
ob.upload_employee_details("raj","c",10000)


