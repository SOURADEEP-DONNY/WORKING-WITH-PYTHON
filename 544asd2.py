f=open("aaa.txt",'r')
for line in f:
    words = line.split()
    for i in words:
        for letter in i:
            if(letter.isdigit()):
                print(letter)
