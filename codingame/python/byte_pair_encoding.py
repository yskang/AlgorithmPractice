import sys
import math
from collections import defaultdict
from string import ascii_letters

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, m = [int(i) for i in input().split()]
line = ''
for i in range(n):
    line += input()

unused_chars = list(ascii_letters)
words = defaultdict(lambda: None)

while True:
    pairs = defaultdict(lambda: [0, 0, 0])
    max_pair = ''
    max_pair_num = 0

    for i in range(len(line)):
        pair = line[i:i+2]
        if pair in pairs:
            if i - pairs[pair][0] > 1:
                pairs[pair][1] += 1
                pairs[pair][0] = i
        else:
            pairs[pair][0] = i
            pairs[pair][1] += 1
            pairs[pair][2] = i

        if max_pair_num < pairs[pair][1]:
            max_pair_num = pairs[pair][1]
            max_pair = pair
        elif max_pair_num == pairs[pair][1] and pairs[pair][2] < pairs[max_pair][2]:
            max_pair_num = pairs[pair][1]
            max_pair = pair

    if max_pair_num == 1:
        break

    new_char = ''
    while unused_chars:
        new_char = unused_chars.pop()
        if new_char not in line:
            break
    
    line = line.replace(max_pair, new_char)
    words[new_char] = max_pair

print(line)
for word in words:
    print(f'{word} = {words[word]}')