N=int(input())
R1,R2=input().split()
Revenue=int(input())
#===========================INPUTS ACCORDINGLY======================================================
#==========================CONVERTING RATES TO INT VALUES===========================================
R1=int(R1)
R2=int(R2)

#===================================================================================================
cost=0
final=0
list1=[31,28,31,30,31,30,31,31,30,31,30,31]  # total days in every month.
list2=[] # for calculating total patients in each month day by day.]
list3=[] # storing 12 lists each representing total number of patients each day
         # within itself.
#====================================================================================================
for j in range(len(list1)):               # ITERATING THROUGH THE LIST CONTAINING LAST DATES MONTHLY.
    for k in range(1,list1[j]+1):         # ITERATING THROUGH EACH DAY IN A MONTH.
        list2.append(((6-j)**2)+abs(k-15))
    list3.append(list2)
    list2=[]
#=====================================================================================================

for i in range(N+1):  # ITERATING THROUGH ALL THE ROOMS
    for j in list3:   # ITERATING THROUGH ACH MONTH FROM THE LIST CONTAINING PATIENT DATA FOR 12 MONTHS
        for k in j:   # ITERATING THROUGH EVERYDAY IN A LIST OF A MONTH

#======================================================================================================
            if k>=N:
                t=N-i
                cost=cost+(i*R1+t*R2)     # CASE 1

#=======================================================================================================
            else:
                h=N-i
                t=k-h


                if t<=0:
                    cost=cost+(k*R2)             # CASE 2
                else:
                    cost=cost+(t*R1+h*R2)        # CASE 3

#===================FINAL AMOUNT CALCULATION FOR EACH MONTH==============================================

        final=final+cost
        cost=0
#=================================CHECKING WHETHER TARGET HAS BEEN MET OR NOT=============================
    if final>=Revenue:    # IF TARGET HAS BEEN MET OR EXCEEDS THE TARGET
        print(i)          # PRINTING THE NUMBER OF TVs REQUIRED.
        break
    else:                 # MEETING THE TARGET REVENUE IS NOT POSSIBLE THEN
        final=0           # INITIALIZING FINAL AMOUNT TO ZERO

else:
    print(N)              # PRINTING THE TOTAL NUMBER OF ROOMS PRESENT.
#=========================================================================================================
