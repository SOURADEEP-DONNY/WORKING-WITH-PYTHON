class car:
    def __init__(self,speed,color):
        self.speed=speed  
        self.color=color  

    def set_speed(self,value):
        self.speed=value

    def get_speed(self):
        return self.speed
        

maruti=car(200,'blue')
bmw=car(500,'black')
TATA_safari=car(450,'maroon')

print(TATA_safari.get_speed())
print(bmw.get_speed())
print(maruti.get_speed())


TATA_safari.speed=900
bmw.speed="NULL"

print(TATA_safari.get_speed())
print(bmw.get_speed())
print(maruti.get_speed())






print("\n\n")
# NOW DATA GETTING PROTECTION



class car:
    def __init__(self,speed,color):
        self.__speed=speed  # Making it Private
        self.__color=color  # Making it Private

    def set_speed(self,value):
        self.__speed=value

    def get_speed(self):
        return self.__speed
        

maruti=car(200,'blue')
bmw=car(500,'black')
TATA_safari=car(450,'maroon')

print(TATA_safari.get_speed())
print(bmw.get_speed())
print(maruti.get_speed())


TATA_safari.speed=900
bmw.speed="NULL"

print(TATA_safari.get_speed())
print(bmw.get_speed())
print(maruti.get_speed())



#clearly no security

