class Car:
    noOfWheels = 4
    def __init__(self,make,model):
        self.make = make
        self.model = model
        
    def setYear(self,year):
        self.__year = year
        
    def getYear(self):
        return self.__year
        
    def print(self):
        print("The Car print:")
        print("The make of the car is: ",self.make)
        print("The model of the car is: ",self.model)
        print("The year it was made was: ", self.__year)
        
    def age(self):
        return (2024-(self.__year))
        
class ElectricCar(Car):
    def __init__(self,make,model,batterySize):
        self.batterySize = batterySize
        super().__init__(make,model)
        
    def print(self):
        print("\n\nThe Electric Car print:")
        print("The make of the car is: ",self.make)
        print("The model of the car is: ",self.model)
        print("The battery size of the car is: ",self.batterySize)
        
        
c = Car("Audi", "A6")
c.setYear(1993)
print("The year it was made has been set to: ",c.getYear())
c.print()
print("The number of the wheels is: ",Car.noOfWheels)
print("The age of the car is: ",c.age())

e = ElectricCar("Toyota","B60", 230)
e.print()


    
