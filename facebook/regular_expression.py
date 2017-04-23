import re
p = re.compile('b*a*.a*.')
result = p.match('bbbaaaacac')
print(result)
