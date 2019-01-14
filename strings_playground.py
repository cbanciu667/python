import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
lines = []

for line in sys.stdin:
    lines.append(line.rstrip())
lines_count = lines[0]
lines.pop(0)
for line in lines:
    counter = 0
    even_chars = []
    odd_chars = []
    for line_char in line:
        if counter%2 == 0:
            even_chars.append(line_char)
        else:
            odd_chars.append(line_char)
        counter += 1
    even_string = ''.join(even_chars)
    odd_string = ''.join(odd_chars)
    even_string = even_string.strip()
    odd_string = odd_string.strip()
    print(even_string,odd_string)


# reversing list to string
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    counter = len(arr)
    resulting_arr = list(reversed(arr))
    print(' '.join(str(x) for x in resulting_arr))
