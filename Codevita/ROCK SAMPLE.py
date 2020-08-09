S,r=input().split()  # TAKING THE TOTAL NUMBER OF SAMPLES AND TOTAL TEST RANGRS AS SPACED I/Ps
#========DECLARING THE TWO IMPUTS AS SPACED INPUTS========================================
S=int(S)
r=int(r)
if S>=10 and S<=10000:
    if r>=1 and r<=1000000:
#============================CHECKING CONSTRAINT CONDITIONS===============================        
        sample=[]                                 # TAKING THE LIST OF SIZES AS SPACED
        count_list=[]                             # APPENDING THE COUNTED RESULTS IN A LIST
#==========================================================================================
        sample=[int(i) for i in input().split()]    # LIST SPACED I/Ps
        for p in range(r):                          # NUMBER OF RANGE LOOPS
            lower,upper=input().split()             # MAX AND MIN RANGES AS SPACED INPUTS
            lower=int(lower)
            upper=int(upper)
            count=0                                 # COUNTING VARIABLE
            for j in range(lower,upper+1,1):
                for k in sample:
                    if k == j:
                        count=count+1               # COUNTER
            count_list.append(count)                # APPENDING THE COUNTS IN A LIST.
        for i in count_list:                        # UNPACKING THE LIST.
            print(i,end=' ')                        # PRINTING THE COUNTS SPACED AS REQUIRED.
#=============================================================================================
