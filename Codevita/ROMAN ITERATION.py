b36=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
roman_numbers=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]


#=========================CONVERTING TO ROMAN=============================================================================================================================
def convert_to_roman(n):
    str1=''
    number_list=[1,4,5,9,10,40,50,90,100,400,500,900,1000] 
    i = 12
    while n: 
        div = n // number_list[i]
        n =n % number_list[i]
        while div:
            str1=str1+roman_numbers[i] 
            div = div - 1
        i=i-1
    return str1
#==========================================================================================================================================================================        
#======================================================CHECKING THE LIMITS ACCORDINGLY=====================================================================================
n=int(input())
if n>3999 or n<1:
    print(n)         # ATP if number is not between 1 and 3999 then print it as it is.
else:
    while(True):                 # while n is not equal to zero.
        if n<4000 and n>0:       # n lies within the range 1-3999
            sum1=0
            p=convert_to_roman(n)           # converting the number to roman number


#======================================================FIXING THE PLACE VALUE ===============================================================================================
            for i in ["X","V","M","L","I","D","C"]:          # since 'X' has the highest place value from elements36 and C has lowest placevalue.So, they are in this order.
                if i in p:
                    d=i
                    break
#============================================================================================================================================================================

            k=b36.index(d)+1
            w=len(p)-1
            for i in p:
                sum1+=(b36.index(i))*(k**w)
                w=w-1
            n=sum1
        else:
            print(n)
            break
#============================================================================================================================================================================
