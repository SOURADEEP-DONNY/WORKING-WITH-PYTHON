class Product:
    def __init__(self,productName,productType,unitPrice,qtyOnHand):
        self.productName=productName
        self.productType=productType
        self.unitPrice=unitPrice
        self.qtyOnHand=qtyOnHand

class Store:
    def __init__(self,productList):
        self.productList=productList

    def productPurchase(self,name,qtyPur):
        for i in self.productList:
            if i.productName == name:
                if i.qtyOnHand==0:
                    return None
                elif i.qtyOnHand>=qtyPur:
                    bill=i.unitPrice*qtyPur
                    i.qtyOnHand-=qtyPur
                    return bill
                else:
                    bill=i.unitPrice*i.qtyOnHand
                    i.qtyOnHand=0
                    return bill
        else:
            return None
                
if __name__ == '__main__':
    n=int(input())
    productList=[]
    for i in range(n):
        productName=input()
        productType=input()
        unitPrice=int(input())
        qtyOnHand=int(input())
        p=Product(productName,productType,unitPrice,qtyOnHand)
        productList.append(p)
    obj=Store(productList)
    pname=input()
    reqdqty=int(input())
    res=obj.productPurchase(pname,reqdqty)
    if res==None:
        print("Product is Not Available")
        for i in obj.productList:
            print(i.productName,i.qtyOnHand)
    else:
        print(res)
        for i in obj.productList:
            print(i.productName,i.qtyOnHand)
