import pyodbc
import schema2
#python open database connectvity
#from Emp import Emp_Details
# declare Global variables used connect to DB
server = 'HCL-02-123\SQLEXPRESS'
database = 'Emp123'
username = 'Rajyalakshmi'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Existing(Exception):
    pass
class Not_in_Range(Exception):
    pass
class Employee_data:
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,Name,Salary,Project,Emp_Id):
        self.Name=Name
        self.Salary=Salary
        self.Project=Project
        self.Emp_Id=Emp_Id
    def insert_values_in_table(self):
        try:
            query = '''  
                            INSERT INTO Employee_Info (Name, Salary, Project,Emp_Id)
                            VALUES
                            ('{0}',{1},'{2}',{3})  '''

            insertQuery = query.format(self.Name, self.Salary, self.Project,self.Emp_Id)
            cursor.execute(insertQuery)
            cnxn.commit()
            print("1 row inserted")
        except:
            print("Primary key not accept the same values")
    def Update_Salary1(self,New_Salary,Name):
        try:
            self.New_Salary = New_Salary
            self.Name=Name
            if self.New_Salary != self.Salary:
                fileinfoQuery = '''
                                                Update Employee_Details SET Salary ='{0}' WHERE Name = '{1}'
                                                '''
                updateQuery = fileinfoQuery.format(New_Salary,self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise Existing
        except Existing:
            print("No Change in Salary")
    def Bonus(self,bonus,Name):
        self.bonus=bonus
        self.Name=Name
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise Not_in_Range
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update Employee_details SET Salary ='{0}' WHERE Name = '{1}'
                                                                '''
                updateQuery = Query.format(self.Salary, self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
        except Not_in_Range:
            print("Bonus is Not in Range")
    def Changeproject(self,project,Name):
        self.project=project
        self.Name=Name

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Employee_details SET Project ='{0}' WHERE Name = '{1}' '''
                updateQuery = Query.format(project, Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Displaydetails(self):
        query=''' select * from Employee_details WHERE Name='{0}' '''
        query1=query.format(self.Name)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}".format(details.Name , details.Salary , details.Project))
    def DeleteEmployeetable(self):
        Query = ''' delete from Employee_details where Name='Usman'  '''
        cursor.execute(Query)
        cursor.commit()
        print("Employee has been deleted")

obj1=Employee_data("layka",30000,"c",105)
obj1.insert_values_in_table()
obj=schema2.employee_table()

obj.Employee_Info()

obj1.insert_values_in_table()
obj1.Update_Salary1()
obj1.Bonu()
obj1.Changeproject()
obj1.Displaydetails()
obj1.DeleteEmployeetable()