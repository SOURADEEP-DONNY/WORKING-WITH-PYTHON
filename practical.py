letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters=sorted(letters,reverse=True)
print(sorted_letters)
animals_sorted=[]
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted=sorted(animals)
print(animals_sorted)
alphabetical={}
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical=sorted(medals.keys())
print(alphabetical)
top_three=[]
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
medal_count=sorted(medals , reverse=True, key = lambda i:medals[i])
top_three.append(medal_count[0])
top_three.append(medal_count[1])
top_three.append(medal_count[2])
print(top_three)

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed=sorted(groceries,  key=lambda i:groceries[i], reverse=True)
print(most_needed)
sorted_ids=[]
ids=[]
def last_four(x):
    ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
    for i in ids:
        lst.append(i%10000)
        sorted_ids=sorted(lst,reverse=False)
    return sorted_ids
