class Product:
    def __init__(self,productName,productType,productPrice,quantityOnHand,reorderedQuantity):
        self.productName=productName
        self.productType=productType
        self.productPrice=productPrice
        self.quantityOnHand=quantityOnHand
        self.reorderedQuantity=reorderedQuantity

def findAvailableStock(productList,lpn):
    lname=[]
    lcoun=[]
    c=0
    for i in productList:
        for j in lpn:
            if i.productName == j:
                lname.append(i.productName)
                lcoun.append(i.quantityOnHand)
                c=c+1
    data=dict(zip(lname,lcoun))
    if c==0:
        return None
    else:
        return data


def updateStockByProductType(productList,num,ptype):
    lname=[]
    lqty=[]
    c=0
    for i in productList:
        if i.productType==ptype:
            c=c+1
            if num > i.quantityOnHand:
                i.quantityOnHand=i.quantityOnHand+num
            else:
                i.quantityOnHand=i.quantityOnHand + 0
        lname.append(i.productName)
        lqty.append(i.quantityOnHand)
    data=dict(zip(lname,lqty))
    if c==0:
        return None
    else:
        return data

if __name__=='__main__':
    n=int(input())
    productList=[]
    for i in range(n):
        productName=input()
        productType=input()
        productPrice=int(input())
        quantityOnHand=int(input())
        reorderedQuantity=int(input())
        b=Product(productName,productType,productPrice,quantityOnHand,reorderedQuantity)
        productList.append(b)
    no=int(input())
    lpn=[]
    for i in range(no):
        lpn.append(input())
    num=int(input())
    ptype=input()
    res=findAvailableStock(productList,lpn)
    res1=updateStockByProductType(productList,num,ptype)
    if res==None:
        print('Product Not Found')
    else:
        for i in res:
            print(i,res[i])
    if res1==None:
        print('Product Not Found')
    else:
        for i in res1:
            print(i,res1[i])
        
