class product:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color="red"
    def display(self):
        print("name of a product=",self.name)
        print("price is=",self.price)
        print("color is=",self.color)
class car(product):
    def __init__(self,name,price,color,milage):
     product.__init__(self,name,price,color)
     self.milage=milage
    def Getmilage(self):
        print("milage  follows=",self.milage)
        print("hello the car information")
        print("price",self.price)
class Bike(car):
    def __init__(self,name,price,color,milage):
     car.__init__(self,name,price,color,milage)
     self.milage=milage
    def Display(self):
        print("milage follows=",self.milage)
p=product("honda",40000,"red")
p.display()
c=car("bmw",225000,"gray",20)
c.display()
c.Getmilage()
b=Bike("xl1000",200000,"black",1000)
b.display()
b.Display()

