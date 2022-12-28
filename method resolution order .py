###c1==>c2,c3(are the child class )==>> c45 is the another class to access the properties of a c2 or c3.
class production:
    def __init__(self,pname,p_price,rating,year):
        self.pname=pname
        self.p_price=p_price
        self.rating=rating
        self.year=year
    def display(self):
        print("product name=",self.pname)
        print("the price of product=",self.p_price)
        print("rating of a product=",self.rating)
        print("year of manifacturing=",self.year)
    def Getrating(self):
        print("rating of a product=", self.rating)
    def Getprice(self):
        print("price of a product=",self.price)
class car(production):
    def __init__(self,pname,p_price,rating,year,milage,typeoffuel):
        production.__init__(pname,p_price,rating,year)
        self.milage=milage
        self.typeoffuel=typeoffuel
    def Getmilage(self):
        print("the milage of a car=1",self.milage)
    def getfueltype(self):
        print("the fueltype=2",self.typeoffuel)
class bike(production):
    def __init__(self,pname,p_price,rating,year,color):
        production.__init__(self,pname,p_price,rating,year)
        self.color="color"
    def Getcolor(self):
        print("the color of a bike=1.1",self.color)
    def Getmilage(self):
        print("the milage of a car=1.2",self.milage)
    def getfueltype(self):
        print("the fueltype=",self.typeoffuel)
class cycle(car,bike):
    pass
p=production("xlcc100",60000,4,2022)
p.display()
obj=car("suresh",23,44,21,21,5,2033)
c=cycle()
c.getfueltype()


