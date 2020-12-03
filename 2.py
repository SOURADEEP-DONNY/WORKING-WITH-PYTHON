T=int(input())
n=int(input())
s=input()
if T>=1 and T<=10:
    if n>=1 and n<=100000:
        s=list(s)
        r=1
        for i in range(n-2):
            if s[i]=='0' and s[i+1]=='1' and s[i+2]=='0':
                r=r+1
        print(r)
