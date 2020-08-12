import math
normal_bulb=[int(i) for i in input().split()]
cfl=[int(i) for i in input().split()]
led=[int(i) for i in input().split()]
list1=[]
list3=[]

for i in range(5):
    hr_charge_perday=int(input())
    list1.append(hr_charge_perday)

    if i==1 or i==2 or i==3:
        list1.append(hr_charge_perday)


for i in list1:
    hr=730*i            # 2 years = 730 days ATP.
    list2=[]

    for j in(normal_bulb,cfl,led):
        if hr<=j[1]:
            cost=j[0]+hr*j[2]
            list2.append(cost)

        # IF WARRANTY PERIOD ENDS BEFORE THEN REPLACEMENT IS NECESSARY.

        else:
            number_of_bulbs_needed=math.ceil(hr/j[1])
            cost=number_of_bulbs_needed*j[0]+hr*j[2]
            list2.append(cost)


    # PICKING THE MINIMUM VALUES.
    list3.append(min(list2))
##print(list3)
print(sum(list3))
                
