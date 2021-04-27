class Product:
    def __init__(self,productName,productType,unitPrice,qtyOnHand):
        self.productName=productName
        self.productType=productType
        self.unitPrice=unitPrice
        self.qtyOnHand=qtyOnHand

class Store:
    def __init__(self,productList):
        self.productList=productList

    def purchaseProduct(self,pname,qpur):
        l=[]
        for i in productList:
            if pname == i.productName:
                if i.qtyOnHand ==0:
                    return None
                elif qpur > i.qtyOnHand:
                    bill=(i.unitPrice*i.qtyOnHand)
                    return bill
                else:
                    bill=(i.unitPrice*qpur)
                    i.qtyOnHand=i.qtyOnHand-qpur
                    return bill
        else:
            return None
if __name__=='__main__':
    n=int(input())
    productList=[]
    for i in range(n):
        productName=input()
        productType=input()
        unitPrice=int(input())
        qtyOnHand=int(input())
        b=Product(productName,productType,unitPrice,qtyOnHand)
        productList.append(b)
    obj=Store(productList)
    pname=input()
    qpur=int(input())
    res=obj.purchaseProduct(pname,qpur)
    if res==None:
        print('Product Not Available')
        for i in obj.productList:
            print(i.productName,i.qtyOnHand)
    else:
        print(res)
        for i in obj.productList:
            print(i.productName,i.qtyOnHand)
