#=====================================================================
# TOTAL NUMBER OF MINIMUM DENOMINATIONS POSSIBLE
# WITH NUMBER OF TEST CASE VALUES.
#=====================================================================

test=int(input("\n TOTAL NUMBER OF TEST CASES "))
if test>=1 and test<=100:
    for i in range(1,test+1):
        max_p=int(input('\n ENTER MAX PRICE FOR DENOMINATION '))
        count=0
        while max_p!=0:
            max_p=max_p//2
            count=count+1

        print("Denominations ",count)
#====================================================================
