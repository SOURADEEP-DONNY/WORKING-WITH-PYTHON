output=""
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output=nested[1][2]
print(output)

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow=True
if lst[2][1]=='yellow':
    print(yellow)
#Test to see if 4 is in the second list of lst. Save to variable ``four``
four=True
if 4 in lst[1]:
    print(four)
four=False
print(four)
#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange=True
if lst[0][1]=='orange':
    print(orange)

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1=True
for i in L:
    if i =='hola':
        print(test1)
    test1=False
    print(test1)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2=True
k=[5,8,7]
for i in L:
    if k in L:
        print(test2)
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3=True
p=6.6
for i in L:
    if p in L:
        print(test3)
london_gold=0
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
for i in nested_d.keys():
    if i=='London':
        
        print(nested_d[i])
        for p in nested_d[i].keys():
            if p == 'Great Britain':
                london_gold=nested_d[i][p]
                print(london_gold)
                

sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1='backstroke'
p=True
for i in sports.values():
    for j in i:
        if j==v1:
            print(v1)
            print(p)
            
# Assign the string 'platform' to the name v2
v2='platform'
p=True
for i in sports.values():
    for j in i:
        if j==v2:
            print(v2)
            print(p)

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3=['vault', 'floor', 'uneven bars', 'balance beam']
p=True
for i in sports.values():
    if i==v3:
        print(v3)
        print(p)
# Assign the string 'rings' to the name v4
v4='rings'
p=True
for i in sports.values():
    if type(i) == dict:
        for j in i.values():
            if j == 'rings':
                print(v4)
                print(p)

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []


for i in nested_d.values():
    #print(i)
    for j in i.keys():
        if j=='USA':
            US_count.append(i[j])
print(US_count)

t=[]
other=[]
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
for i in athletes:
    for j in i:
        if 't' in j:
            t.append(j)
        else:
            other.append(j)
print(t)
print(other)
third=[]
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
for i in l_of_l:
    third.append(i[2])
    
print(third)

