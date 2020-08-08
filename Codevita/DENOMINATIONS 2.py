number=int(input())
if number>0 and number<1000:
    total=0
    five=((number-4)//5)
    if(number-4-(5*five))%2 == 0:
        one = 2
    else:
        one = 1
    two=(number-(five*5)-(one*1))//2
    total=five+one +two
    print(total,five,two,one)
