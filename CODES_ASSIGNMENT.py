def mult(i,d=6):
    return i*d
print(mult(5))

def greeting(greeting="Hello ", name='', excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false

c_false=(checkingIfIn('lichu'))
# Call the fucntion so that it returns True and assign it to the variable c_true
fruit_ans=(checkingIfIn('fruit'))
# Call the function so that the value of fruit is assigned to the variable fruit_ans
c_true=(checkingIfIn(direction=False,a='apples'))
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check=(checkingIfIn('watermelon'))+1
def test(a,b=True,dict1={2:3, 4:5, 6:8}):
    if b==True:
        for i in dict1.keys():
            if a==i:
                return dict1[i]
    return False

def sum(intx,intz=5):
    return intz + intx

def mult(i,d=6):
    return i*d
print(mult(5))
