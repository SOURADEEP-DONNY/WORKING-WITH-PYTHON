a=[]

def push_stack(e):
    a.append(e)
    
def pop_stack():
    if len(a)<=0:
        print("List is empty")
    else:
        return a.pop(0)
    
def display_stack():
    for i in range(len(a)-1,-1,-1):
        print(a[i])
push_stack(24)
push_stack(2)
display_stack()
pop_stack()
display_stack()
push_stack(5)
push_stack(7)
display_stack()
pop_stack()
display_stack()

    


        
        
    
