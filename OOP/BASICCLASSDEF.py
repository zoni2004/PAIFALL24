class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def print(self):
        print("The make of the car is: ",self.make)
        print("The model of the car is: ",self.model)
        print("The year it was made was: ", self.year)
        
c = Car("Audi", "A6", 2003)
c.print()
