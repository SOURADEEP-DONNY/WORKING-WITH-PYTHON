#============CONVERTING NUMBER TO ROMAN NUMBERS=================================

roman_numbers=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
def convert_to_roman(n):
    str1=''
    number_list=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    i=12
    while(n):
        div=n//number_list[i]
        n=n%number_list[i]
        while div:
           str1=str1+roman_numbers[i]
           div=div-1
        i=i-1
    return str1

number=int(input())
print(convert_to_roman(number))

#=============================================================================
