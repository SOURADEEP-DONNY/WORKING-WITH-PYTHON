def hcf(n1,n2):
    if n2==0:
        return n1
    return hcf(n2,n1%n2)




print(hcf(30,36))
