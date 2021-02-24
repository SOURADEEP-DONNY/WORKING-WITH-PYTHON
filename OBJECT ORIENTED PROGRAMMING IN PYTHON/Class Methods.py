class ABC:
    counter=0
    def __init__(self):
        ABC.counter+=1
    @classmethod
    def counter_function(cls):
        return f'You have created {ABC.counter} objects/instances'

obj1=ABC()
obj2=ABC()
print(ABC.counter_function())
