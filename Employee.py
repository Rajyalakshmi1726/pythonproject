import pyodbc #python open database connectvity
#from Emp import Emp_Details
# declare Global variables used connect to DB
server = 'HCL-02-123\SQLEXPRESS'
database = 'Emp123'
username = 'Rajyalakshmi'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class employee_schema:
    def employe_table(self):
        try:
            query1 = cursor.execute('''use Emp123''')
            query2 = cursor.execute('''create table Employee_Info(
            Emp_Id int NOT NULL,
            Name varchar(50),
            project varchar(50),
            salary int,
            primary key (Emp_Id)
            )
            ''')
            query3 = cursor.execute('''select * from Employee_Details''')
            cnxn.commit()
            print("Table created sucessfully")
        except:
            print("the table is already exits")
obj=employee_schema()
obj.employe_table()