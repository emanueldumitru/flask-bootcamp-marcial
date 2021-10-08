import re


pattern = re.compile('this')
another_pattern = re.compile(r"([a-zA-Z]).([a])") # r stands for raw string
string = 'search this inside of this text please'
print ( 'search' in string)
#re.search('this', string)
a = pattern.search(string)
# print (a.group())
b = pattern.findall(string)
c = pattern.fullmatch(string) #it has to be the exactly same string
print(b)
print(c)

print (a.group())