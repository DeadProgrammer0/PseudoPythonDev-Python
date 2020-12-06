# Re module 

import re

mystr ='''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Ms. 420
'''

# pattern = re.compile(r'\w+\.\w[a-zA-Z]+')

# matches = pattern.finditer(mystr)

# for match in matches:
#     print(match)


# pattern = re.compile(r'\d{3}\W\d{3}\W\d{4}')
# pattern = re.compile(r'[89]00\W\d{3}\W\d{4}')

# matches = pattern.finditer(mystr)

# for match in matches:
#     print(match)


# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s(\w)+')

# matches = pattern.finditer(mystr)

# for match in matches:
#     print(match)

# with open('Regex Data\data.txt','r',encoding='utf-8') as f:
#     mystr2 = f.read()

# pattern = re.compile(r'\d{3}\W\d{3}\W\d{4}')
# matches = pattern.finditer(mystr2)

# for match in matches:
#     print(match)

# pattern = re.compile(r'\d{3}\s\w+\s\w+\.,\s\w+\s\w+\s\d{5}')
# matches = pattern.finditer(mystr2)

# for match in matches:
#     print(match)


# pattern = re.compile(r'\w[a-zA-Z]+\s\w[a-zA-Z]+\n')
# matches = pattern.finditer(mystr2)

# for match in matches:
#     print(match)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net.in
'''
# pattern = re.compile(r'.+@[a-zA-Z-+_.]+\.\w+')
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.us.gov
'''

# pattern = re.compile(r'\w+://(www\.)?[a-zA-Z-+_.]+\.\w+')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match)


sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)

