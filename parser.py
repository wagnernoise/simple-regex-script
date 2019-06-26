'''
A little program to strip the serial part "==00.00.00"
from some requirement files. Sometimes this is a problem
since (many times) there are packages deprecated in those
requirement lists. 
Feel free to use it and modify it!
'''

import re
with open('requirements-sample_file-.txt', 'r') as f:
    text = f.read()

pattern = re.compile(r'==\d+.\d+.*\d*')   
new_text = pattern.sub('', text)

file = open('new_requirements.txt', 'a')
file.write(new_text)
file.close

#print(new_text)
