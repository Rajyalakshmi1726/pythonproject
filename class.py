##car problem by using class :
"""class car_a:

    color="red"
    max_speed=100
    tyrefriction=40
    strat_engine=False
    current_speed=200
    def startEngine(self):
        self.start_engine=True
        print("car engine is on")
    def stopEngine(self):
        self.start_engine=False
        print("car engine is off")

    def applyBrakes(self,tyrefriction):

        self.tyrefriction=tyrefriction
        self.current_speed -= self.tyrefriction
        if self.current_speed > self.max_speed:
            self.current_speed=self.max_speed
            print("APPLY BREAK AND STOP.")

    def accleration(self):
        pass
    def soundHorn(self):
        if self.start_engine == True:
            print("Beep Beep")
        else:
            print("cat not started")
s=car_a()
s.startEngine()
s.stopEngine()
s.applyBrakes(50)
s.startEngine()
s.soundHorn()"""




##shoping items in python
product={"mobile"=10000,"Laptop":20000}
cart={}
def add_products(self,item,price):
    self.add_product[item]=price





