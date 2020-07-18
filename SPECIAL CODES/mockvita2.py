N=input('\nEnter the three digit numbers by giving space:')
n1=N.split()
print(n1)
lst=[]
for n_three in n1:
    n_three=int(n_three)
    #print(n_three)
    #n_three=int(input("\nEnter a number:-"))
    maxi=0
    mini=0
    mul_11=0
    mul_7=0
    bit_pairs=0
    bit_score=0
    bit=0

    if n_three>= 100 and n_three<=999:
        n_three=str(n_three)
        p0=n_three[0]
        p0=int(p0)
        p1=n_three[1]
        p1=int(p1)
        p2=n_three[2]
        p2=int(p2)
        #print(p0)
        #print(p1)
        #print(p2)
        maxi=max(p0,p1,p2)
        mini=min(p0,p1,p2)
        #print('maximum',maxi)
        #print('minimum',mini)
        mul_11=maxi*11
        mul_7=mini*7
        #print(mul_11)
        #print(mul_7)

        bit=mul_11 + mul_7
        #print('Bit',bit)
        if bit>=100:
            bit=str(bit)
            bit_score=bit[1:]
            lst.append(bit_score)
            print('Bit score 3=',bit_score)
        else:
            bit_score=bit
            lst.append(bit_score)
            print('Bit Score 2=',bit_score)
print(lst)
lst2=[]
lst3=[]
p=0
l1=[]
l2=[]
for i in lst:
    k=lst.index(i)
    if k%2==0:
       lst2.append(lst[k])
    else:
        lst3.append(lst[k])
print('EVEN',lst2)
print('ODD',lst3)
for i in lst2:
    i=int(i)
    q=i//10
    l1.append(q)
for i in lst3:
    i=int(i)
    q=i//10
    l2.append(q)
print(l1)
print(l2)
