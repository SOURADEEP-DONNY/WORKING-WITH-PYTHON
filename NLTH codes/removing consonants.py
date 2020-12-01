vowel=['a','e','i','o','u','A','E','I','O','U']
str1=input()
new_str=""
for i in str1:
    if i in vowel:
        new_str=new_str+i

print(new_str)
