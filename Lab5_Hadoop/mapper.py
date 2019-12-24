%%writefile mapper.py
#!/usr/bin/env python
# MAPPER

import csv
import sys
import re

lines = sys.stdin.readlines()

csvreader = csv.reader(lines)
# YOUR CODE GOES BELOW

# Create a list of ONLY the comments using a list comprehension
comments = [row[3] for row in csvreader]

# Iterate over each of the comments
for comment in comments:
    # Split the comment string into words, using every whitespace character as a divider. 
    tokens = re.split("\s", comment)
    for token in tokens:
        #Print the key, value pair <token, 1>
        print(token + "\t1")
        
