Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits=0
for i in Junior:
    credits=credits+Junior[i]
print(credits)
str1 = "peter piper picked a peck of pickled peppers"
freq={}
for i in str1:
    if i not in freq:
        freq[i]=0
    freq[i]=freq[i]+1
print(freq)
s1 = "hello"
counts={}
for i in s1:
    if i not in counts:
        counts[i]=0
    counts[i]=counts[i]+1
print(counts)
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words={}
l=str1.split()
for i in l:
    if i not in freq_words:
        freq_words[i]=0
    freq_words[i]=freq_words[i]+1
print(freq_words)
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d={}
donny_list=sent.split()
for i in donny_list:
    if i not in wrd_d:
        wrd_d[i]=0
    wrd_d[i]=wrd_d[i]+1
print(wrd_d)
sally = "sally sells sea shells by the sea shore"
characters={}
for _ in sally:
    if _ not in characters:
        characters[_]=0
    characters[_]=characters[_]+1
print(characters)
keys=list(characters.keys())
best_char=keys[0]
for __ in keys:
    if characters[__]>characters[best_char]:
        best_char=__
print(best_char)
sally = "sally sells sea shells by the sea shore and by the road"
characters={}
for _ in sally:
    if _ not in characters:
        characters[_]=0
    characters[_]=characters[_]+1
print(characters)
keys=list(characters.keys())
worst_char=keys[0]
for __ in keys:
    if characters[__]<characters[worst_char]:
        worst_char=__
print(worst_char)
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts={}
for i in string1:
    p=i.lower()
    if p not in letter_counts:
        letter_counts[p]=0
    letter_counts[p]=letter_counts[p]+1
print(letter_counts)
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d={}
for i in p:
    pr=i.lower()
    if pr not in low_d:
        low_d[pr]=0
    low_d[pr]=low_d[pr]+1
print(low_d)

