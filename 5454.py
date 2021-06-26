class Car:
    kind ='car'
    def __init__(self,color,name):
        self.color=color
        self.name=name

def honk(self):
    print('Beep, Im'+ self.color)

class RedCar(Car):
    def __init__(self):
        Car.__init__(self,'red','redCar')
        self.age=10

class BlueCar(Car):
    def honk(self):
        print('Beep Beep!')
car1= Car('black','jaguar')
print(Car.name)
