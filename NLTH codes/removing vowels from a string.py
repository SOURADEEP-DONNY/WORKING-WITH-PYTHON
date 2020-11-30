vowel=['a','e','i','o','u','A','E','I','O','U']
str1=input()
new_str=''
for i in str1:
    if i not in vowel:
        new_str=new_str+i

##    if i in vowel:
##        print(i,'is a vowel')

print(new_str)
