def calculate(number):
    if number<10:
        print (number + 10)
        return
    l=[]
    for i in range(9,1,-1):
        while number%i == 0:
            number=number/i
            l.append(i)
    if number>10:
        print('Not Possible')
        return
    l.reverse()
    s1=[str(i) for i in l]
    s2=''.join(s1)
    print(int(s2))

n=int(input())
calculate(n)
