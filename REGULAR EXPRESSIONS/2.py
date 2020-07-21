#==================================LITERAL MATCHING=============================
import re
print(re.search('Dy','Donny is Souradeep.'))
print(re.search('D|y','Donny is Souradeep.')) #will only get the first instance.

#TO FIND EVERY INSTANCES WE NEED TO USE 're.findall'
#IT RETURNS A LIST OF ALL THE ELEMENTS.
print(re.findall('D|y','Donny is Souradeep.'))
print(re.findall('e','Donny is Souradeep.'))
print(re.findall('deep','deep is Souradeep.'))
