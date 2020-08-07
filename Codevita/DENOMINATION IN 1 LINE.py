#=====================DENOMINATIONS IN ONE LINE================================
test=int(input("\nENTER TOTAL TEST CASES:-"))
if test>=1 and test<=100:
    for i in range(1,test+1):
        print(len("{0:b}".format(int(input("\nENTER AMOUNT ")))))
else:
    print("\nSORRY OUT OF RANGE!!!")
#==============================================================================
