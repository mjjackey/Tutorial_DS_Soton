%%writefile reducer.py
#!/usr/bin/env python
# REDUCER

import sys
from collections import defaultdict
# Keep simple example in for now, switch to stdin later

input_pairs = [
    '+447935454150	1',
    'lovely	1',
    'girl	1',
    'talk	1',
    'to	1',
    'me	1'
    #'xxx	1',
     #Add an extra one to test that it works
    #'to\t1'
]
# Once we test this with streams, we can uncomment this next line
# input_pairs = sys.stdin.readlines()

# YOUR CODE GOES BELOW

# Create a default dictionary. 
# This is a key-value store (dictionary) which returns a default value if the key hasn't been added.
# Here, we use it to store <word, count> pairs.
accumulator = defaultdict(lambda: 0)

for row in input_pairs:
    # Split the line into our key value pair.
    key_value_pair = row.split("\t", 1)
    
    # If we don't have a pair, ignore the line, as something has gone wrong.
    if len(key_value_pair) != 2:
        continue
    
    # Retrieve the count of that word we've seen so far, add to it, then store the result.
    accumulator[key_value_pair[0]] = accumulator[key_value_pair[0]] + int(key_value_pair[1])
    
for (key, value) in accumulator.items():
    print(key + "\t" + str(value))
