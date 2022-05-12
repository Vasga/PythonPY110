import re

result = re.findall(r'.',"Everest is the biggest mountain in the World")
print(result)
result = re.findall(r'\S',"Everest is the biggest mountain in the World")
print(result)
result = re.findall(r'\w+',"Everest is the biggest mountain in the World")
print(result)
result = re.findall(r'\w*',"Everest is the biggest mountain in the World")
print(result)
result = re.findall(r'\b[E,i]\w+',"Everest is the biggest mountain in the World")
print(result)