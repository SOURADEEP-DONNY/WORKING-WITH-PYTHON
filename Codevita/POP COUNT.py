list1=[1,2,3,1,1,2,3]
count=0
k=0
print('ORIGINAL LIST=',list1)
for i in range(len(list1)):


    # DOING THE POP OPERARTION FROM THE END OF THE LIST AND COUNTING WITH THE POPPED
    # ELEMENT AT THE SAME TIME.
    k=list1.pop()
    print('POPPED ELEMENT',k)
    print(list1)
    for j in list1:
        if k==j:
            count=count+1
print(count)



