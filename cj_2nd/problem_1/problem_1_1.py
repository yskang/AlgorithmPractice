import sys
import math

filename = sys.argv[1]

test_input = open(filename, 'r')

numberOfTests = int(test_input.readline().replace('\n', ''))

xs = []
ys = []
es = []

for testCase in range(numberOfTests):
    line = test_input.readline().replace('\n', '')
    xs.append(int(line.split(' ')[0]))
    ys.append(int(line.split(' ')[1]))
    es.append(int(line.split(' ')[2]))

test_input.close()

output = open(filename.replace('in', 'out'), 'w')

for i in range(numberOfTests):
    a = xs[i]
    b = es[i] - xs[i]
    circle = 2 * math.pi * ys[i]
    alpha = math.atan2(xs[i], ys[i])
    beta = math.atan2(b, ys[i])
    theta = 2 * math.pi - 2 * alpha - 2 * beta
    c = circle * theta / (2 * math.pi)
    output.write(str(int(math.ceil(a + b + c))) + '\n')

output.close()