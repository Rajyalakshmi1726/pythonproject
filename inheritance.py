class product():
    def __init__(self,name,price,dealprice,rating):
        self.name=name
        self.price=price
        self.dealprice=dealprice
        self.rating=rating
    def display(self):
        print(self.name)
        print(self.price)
        print(self.dealprice)
        print(self.rating)

class Electronic(product):
    def __init__(self,name,price,dealprice,rating,warenty):
        super().__init__(name,price,dealprice,rating)
        self.warenty=warenty
    def Getwarenty(self):
         print("warenty",self.warenty)
class Grocery(product):
    def __init__(self,name,price,dealprice,rating,expiredate):
       super().__init__(name, price, dealprice, rating)
       self.expiredate=expiredate
    def getproduct(self):
         print("expiredate=",self.expiredate)
class order():
    def __init__(self,item,ordertype):
p=product("nokia",10000,8000,3)
p.display()
e=Electronic("nokia",10000,8000,3,20)
e.Getwarenty()
e.display()
g=Grocery("nokia",10000,8000,3,2022)
g.getproduct()
g.display()




