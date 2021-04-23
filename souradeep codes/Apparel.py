class Apparel:
    def __init__(self,apparelBrand,Type,price,InStock):
        self.apparelBrand=apparelBrand
        self.Type=Type
        self.price=price
        self.InStock=InStock

class Store:
    def __init__(self,alist):
        self.alist=alist

    def checkApparelAvailability(self,inbrand,aptype,apsize,noofreqd):
        s1=False
        s2=False
        s3=False
        temp=None
        for i in alist:
            if i.apparelBrand == inbrand and i.Type == aptype:
                s1=True
                temp=i.InStock
        if temp is not None:
            if apsize in temp.keys():
                s2=True
                if noofreqd < temp[apsize]:
                    s3 = True
                    temp[apsize]=noofreqd
                    if s1 == True and s2 == True and s3 == True:
                        print('Size is Available')
                        for i,j in temp.items():
                            print(i,':',j)
                        return True
        return False
if __name__=='__main__':
    alist=[]
    num=int(input())

    for i in range(num):
        apparelBrand=input()
        Type=input()
        price=int(input())
        count=int(input())
        dictionary={}
        for i in range(count):
            size=input()
            available=int(input())
            dictionary[size]=available
        b=Apparel(apparelBrand,Type,price,dictionary)
        alist.append(b)
    apbrand=input()
    apType=input()
    apSize=input()
    count=int(input())
    store=Store(alist)
    result=store.checkApparelAvailability(apbrand,apType,apSize,count)

    if result == False:
        print('Size is not available')

    status = False
    for i in alist:
        if i.apparelBrand == apbrand and i.Type == apType:
            status=True
            break

    if status == False:
        print('Apparel not found')




    
