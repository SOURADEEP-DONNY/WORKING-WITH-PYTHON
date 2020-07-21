import re

#SEARCH KEYWORD
print(re.search("Donny","Donny is an engineer"))
print(re.search("table tennis","Donny plays table tennis."))


#MATCH KEYWORD
print(re.match('Donny',"Donny is an engineer"))
print(re.match("table tennis","Donny plays table tennis."))
print(re.match('a',"abcd"))
