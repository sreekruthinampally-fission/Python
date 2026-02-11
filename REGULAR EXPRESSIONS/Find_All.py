import re

s = "GeeksforGeeks : A computer science portal for geeks"
match = re.search(r'portal',s)

print('Start Index :', match.start())
print("End Index :", match.end())

string = """Hello my number is 123 and my friend's number is 987"""

regex = '\d+'
match = re.findall(regex, string)
print(match)

import re
p = re.compile('[a-e]')
print(p.findall("Aye, said Mr.Gibenson Stark"))

p = re.compile('\d')
print(p.findall("I went to him at 11 am on 4th july 1886"))

p =re.compile('\d+')
print(p.findall("I went to him at 11 am on 4th july 1886"))

p = re.compile('ab*')
print(p.findall('ababbaabbb'))

from re import split

print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))
