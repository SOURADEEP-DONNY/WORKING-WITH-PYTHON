class Apparel:
    def __init__(self,apparelBrand,Type,price,InStock):
        self.apparelBrand=apparelBrand
        self.Type=Type
        self.price=price
        self.InStock=InStock

class Store:
    def __init__(self,apparelList):
        self.apparelList=apparelList

    def checkApparelAvailability(self,strbr,strty,strsi,appreqd):
        c1=0
        c2=0
        c3=0
        for i in apparelList:
            if strbr == i.apparelBrand and strty == i.Type:
                c1=c1+1
                for j in i.InStock:
                    if j == strsi:
                        c2=c2+1
                        if i.InStock[j] > appreqd:
                            c3=c3+1
                            i.InStock[j]=i.InStock[j]-appreqd
                            return(i.InStock)
        if c1==0 and c2==0 and c3==0:
            return None
                
if __name__=='__main__':
    n=int(input())
    apparelList=[]
    for i in range(n):
        apparelBrand=input()
        Type=input()
        price=int(input())
        tot=int(input())
        lsize=[]
        lqty=[]
        for j in range(tot):
            size=input()
            qty=int(input())
            lsize.append(size)
            lqty.append(qty)
        InStock=dict(zip(lsize,lqty))
        b=Apparel(apparelBrand,Type,price,InStock)
        apparelList.append(b)
    obj=Store(apparelList)
    strbr=input()
    strty=input()
    strsi=input()
    appreqd=int(input())
    res=obj.checkApparelAvailability(strbr,strty,strsi,appreqd)
    if res==None:
        print('Size is not available.')
        print('Apparel not Found')
    else:
        print('Size is available')
        for i in res:
            print(i,':',res[i])
                        
