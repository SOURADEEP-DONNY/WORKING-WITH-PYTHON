class Laptop:
    def __init__(self,laptop_brand,laptop_model,price):
        self.brand=laptop_brand
        self.model=laptop_model
        self.price=price
        

    def Discount(self,num):
        cal_price=self.price-((num/100)*self.price)
        return(cal_price)


obj1=Laptop('HP','Supermodel',100000)
print(obj1.Discount(50))
