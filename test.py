class parent:



    def display(self):
        print("parent class")
class child1(parent):
    def display(self):
        print("child1 class")

class child2(parent):
    def display(self):
        print("child2 class")
class child3(child2,child1):
    pass
c=child3()
c.display()