class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand=brand_name
        self.model=model_name
        self.price=price

'''CREATING OBJECTS'''
obj1=Laptop('Lenovo','Ideapad100',20000)
obj2=Laptop('HP','supermodel',30000)

print(obj1.brand)
print(obj1.price)
