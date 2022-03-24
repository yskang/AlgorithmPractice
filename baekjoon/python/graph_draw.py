import matplotlib.pyplot as plt

xs = [i for i in range(-10, 111)]

def f0(x: int):
    return 100*x

def f1(x: int):
    return 15*x+100

def f2(x: int):
    return 5*x + 325

fig = plt.figure()
plt.ion()
plt.show()
ax = fig.add_subplot(1,1,1)
ax.axhline(y=0, color='gray', linestyle='--')
ax.axvline(x=0, color='gray', linestyle='--')
ax.plot(xs, list(map(f0, xs)), color='tab:blue')
plt.draw()
plt.pause(0.01)
input()
ax.plot(xs, list(map(f1, xs)), color='tab:cyan')
plt.draw()
plt.pause(0.01)
input()
ax.plot(xs, list(map(f2, xs)), color='tab:green')
plt.draw()
plt.pause(0.01)
input()
ax.plot([0, 10], [0, 20], color='tab:red')
plt.draw()
plt.pause(0.01)
input()
