import re

#SEARCH KEYWORD
print(re.search("Donny","Donny is an engineer"))
print(re.search("table tennis","Donny plays table tennis."))


#MATCH KEYWORD
print(re.match('Donny',"Donny is an engineer"))
print(re.match("table tennis","Donny plays table tennis."))
print(re.match('a',"abcd"))


#BOOLEAN MATCH
print(bool(re.match('Donny',"Donny is an engineer")))
print(bool(re.match("table tennis","Donny plays table tennis.")))
print(bool(re.match('a',"abcd")))


#BOOLEAN SEARCH
print(bool(re.search("Donny","Donny is an engineer")))
print(bool(re.search("table tennis","Donny plays table tennis.")))

#PRINTING INDEX
print(re.search("Donny","Donny is an engineer").start())
print(re.search("Donny","Donny is an engineer").end())
print(re.search("table tennis","Donny plays table tennis.").start())
print(re.search("table tennis","Donny plays table tennis.").end())
