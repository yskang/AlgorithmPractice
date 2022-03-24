import matplotlib.pyplot as plt

f = open('out.txt', 'r')
d = f.readlines()
f.close()

data = list(map(lambda s: int(s.replace(' ', '').replace('\n', '').split(':')[1]), d))

plt.plot(data)
plt.show()