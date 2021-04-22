class Product:
    def __init__(self,productName,productType,productPrice,quantityOnHands,reorderingQuantity):
        self.productName=productName
        self.productType=productType
        self.productPrice=productPrice
        self.quantityOnHands=quantityOnHands
        self.reorderingQuantity=reorderingQuantity

def findAvailableStock(productList,inputList):
    c=0
    for i in inputList:
        for j in productList:
            if i.lower()==j.productName.lower():
                print(i,j.quantityOnHands)
                c=c+1
    if c==0:
        print('Product Not Found')

def updateStockByProductType(productList,quantity,Type):
    c=0
    for i in productList:
        if i.productType.lower()==Type.lower():
            c=c+1
            if i.quantityOnHands <= reorderingQuantity:
                i.quantityOnHands=i.quantityOnHands+quantity

    if c==0:
        print('Product Not Found')
    else:
        for i in productList:
            print(i.productName,i.quantityOnHands)
if __name__=='__main__':
    n=int(input())
    productList=[]
    for i in range(n):
        productName=input()
        productType=input()
        productPrice=int(input())
        quantityOnHands=int(input())
        reorderingQuantity=int(input())
        b=Product(productName,productType,productPrice,quantityOnHands,reorderingQuantity)
        productList.append(b)

    num=int(input())
    inputList=[]
    for i in range(num):
        inputList.append(input())
    findAvailableStock(productList,inputList)
    pquantity=int(input())
    ptype=input()
    updateStockByProductType(productList,pquantity,ptype)



