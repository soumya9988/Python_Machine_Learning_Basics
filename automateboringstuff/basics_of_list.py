a0 = dict(zip(('a','b','c','d','e'), (1,2,3,4,5)))
print(a0)
a1 = range(10)
print(a1)
a2 = sorted([i for i in a1 if i in a0])
print(a2)
a3 = sorted(([a0[i] for i in a0]))
print(a3)

x = ['ad', 'bc']
print(len(list(map(list, x))))

print(~4)
