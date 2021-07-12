a=[]

def push_queue(e):
    a.append(e)
    
def pop_queue():
    if len(a)<=0:
        print("List is empty")
    else:
        return a.pop(0)
    
def display_queue():
    for i in range(len(a)-1,-1,-1):
        print(a[i])
push_queue(24)
push_queue(2)
display_queue()
pop_queue()
display_queue()
push_queue(5)
push_queue(7)
display_queue()
pop_queue()
display_queue()

    


        
        
    
