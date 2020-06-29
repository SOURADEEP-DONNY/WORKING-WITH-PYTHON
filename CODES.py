s=""
num=0
f=open("travel_plans.txt","r")
for i in f:
    for j in i:
        if s=="":
            num=num+1
print(num)
f.close()
num_words=0
f=open("emotion_words.txt",'r')
for i in f:
    for j in i:
        if j==" ":
            num_words=num_words+1
num_words=num_words+7
print(num_words)
num_lines=0
_=open("school_prompt.txt","r")
for __ in _:
    num_lines=num_lines+1
print(num_lines)
#WAP TO PRINT THE FIRST WORD OF EVERY LINE OF A TEXT DOCUMENT IN A LIST.

k=[]
first=[]
f=open('example.txt','r')
for i in f:
    k=i.strip().split()
    first.append(k[0])
print(first)
f.close()
