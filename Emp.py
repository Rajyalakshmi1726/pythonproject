class Emp_Details:
    Bonus = int(input("enter the bonus"))
    project=["Python","c","java"]
    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project
    def Add_Bonus():


        try:


            if Bonus<=2:
                print("the Bonus is")
            else:
                print("the Bonus value is more than 2")
            self.salary = int(input("enter the salary"))
            self.Bonus+=self.salary*self.Bonus
            print("the Bonus of a salary",self.Bonus)
        except:
            print("only enter the less than 2")
    def Update(self):

        self.salary+=self.Bonus
        #print("the updated salary is=",self.salary)
    def Change_project(self):

        try:
            pro=["c#",".net"]
            if self.project == pro:
                print("the projects are same")
            else:
                print("the projects are not same")
        except:
            print("the project is does not matchabove two files")
    def Display(self):
        print("the display method")
        print("the name is",self.name)
        print("the salary is",self.salary)
        print("the project is:",self.project)

op=Emp_Details
op.Add_Bonus()
op.Update()
op.Change_project()
op.Display()



