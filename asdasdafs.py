f=open("Abhi.txt",'r')
s=f.read()
for i in f:
    words=i.split()
    print(words)
