class Car:
    company="TATA" #CLASS VARIABLE
    def __init__(self,speed,rating):
        self.speed=speed
        self.rating=rating
Safari=Car(200,'5 stars')  #INSTANCE VARIABLE
Sumo=Car(140,'4.5 stars')  #   "        "

print(Safari.speed,Safari.rating)
print(Sumo.speed,Sumo.rating)

Car.company="TATA MOTORS"

print(Car.company)
