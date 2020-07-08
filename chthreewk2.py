map_testing=[]
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing=list(map(lambda x:'Fruit: '+x,lst_check))
print(map_testing)
b_countries=[]
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries=list(filter(lambda i: 'b' and 'B' in i,countries))
print(b_countries)
first_names=[]
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names=[i[0] for i in people]
print(first_names)
first_names=[i[1] for i in people]
print(first_names)
lst2=[]
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
for i in lst:
    lst2.append(i*2)
print(lst2)
opposites=[]
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3=list(zip(l1,l2))
for (x1,x2) in l3:
    if x1==3:
        opposites=list(filter(lambda x1,x2:x1==x2))
print(opposites)    
opposites=[]
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3=list(zip(l1,l2))
for (x1,x2) in l3:
    if x1==3:
        opposites=list(filter(lambda x1,x2:x1==x2))
print(opposites)    
