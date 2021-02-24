class ABC:
    counter=0
    def __init__(self):
        ABC.counter+=1

obj1=ABC()
obj2=ABC()
print(ABC.counter)
