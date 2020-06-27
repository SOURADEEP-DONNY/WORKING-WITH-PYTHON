inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
s=",".join(inventory)
#print(s)
new_list=s.split(",")
#print(new_list)
k=[]
kk=[]
kkk=[]
for i in new_list[1::3]:
    
    k.append(i)
    #print(k)
for j in new_list[::3]:
    
    kk.append(j)
    #print(kk)
for jj in new_list[2::3]:
    
    kkk.append(jj)
    #print(kkk)
#print(k)
#print(kk)
#print(kkk)

#print("The store has {} {}, each for {} USD.".format(k[0],kk[0],kkk[0]))

for i in range(4):
    print("The store has{} {}, each for{} USD.".format(k[i],kk[i],kkk[i]))
p_phrase = "was it a car or a cat I saw"
r_phrase=p_phrase[-1::-1]
if r_phrase==p_phrase:
    print("PALLINDROME")
else:
    print("NON-PALLINDROME")
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
l1=scores.split()
a=[]
a_scores=0
for i in l1:
    i=int(i)
    if i>=90:
        a.append(i)
        a_scores=a_scores+1
print(a_scores)
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
l=org.split()
acro=""
#print(l)
for i in l:
    if i not in stopwords:
        acro=acro+(i[0].upper())
print(acro)
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

l=sent.split()
acro=""
#print(l)
for i in l:
    if i not in stopwords:
        acro=acro+(i[0:2].upper())+', '
print(acro)


