N=int(input())
l=[]
for i in range(N):
    l.append(int(input()))
if (N<2):
    print("Invalid Input")
else:
    l.sort()
    if (len(set(l))==1):
        print("Equal")

    else:
        for i in range(N-1):
            if(l[0] != l[i+1]):
                print(l[0],' ',l[i+1])
                break
