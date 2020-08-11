t=int(input())
if t>=1 and t<=100:
    count=0
    list_time=[]
    list_copy=[]
    for i in range(t):
        x,y,speed=[int(i)for i in input().split()]
        time=((x**2)+(y**2))//(speed**2)
        list_time.append(time)
    #print(list_time) #LIST OF TIME OF PASSING.


    
    for j in range(len(list_time)):  # RUNNING A LOOP ENTIRELY IN THE TIME LIST
        k=list_time.pop() #POPPING THE ELEMENT FROM THE END AND STORING THE POPPED ELEMENT INSIDE A VARIAVLE FOR FURTHER COMPARISON.
        for ii in list_time:
            if k==ii:  # COMPARING THE POPPED ELEMENT INSIDE THE POPPED LIST
                count=count+1 # COUNTING THE TIMES THE NUMBER OF TIMES THEY MET.

print(count)
