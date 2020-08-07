test=int(input())

while test>0:
    P=input('\nENTER YOUR ALPHABETICAL ORDER')
    S=input('\nENTER YOUR STRING')
    list1=[]
    for i in S:
        list1.append(P.find(i))  #P.find(i) WILL FIND THE INDEX OF THE ALPHABETS IN THE STRING.
    list1.sort()
    for i in list1:
        print(P[i],end='')

    if test>1:
        print()
    test=test-1
                
