N=int(input())
A=int(input())
one_hund=int(input())
two_hund=int(input())
five_hund=int(input())
thousand=int(input())
maximum_notes=0


for i in range(thousand+1):
    for j in range(five_hund+1):
        for k in range(two_hund+1):
            for l in range(one_hund+1):
                if (i+j+k+l)<=N and (i*1000+j*500+k*200+l*100==A):
                    res=i+j+k+l
                    if maximum_notes<res:
                        maximum_notes = res

if maximum_notes==0:
    print(0)
else:
    print(maximum_notes)
