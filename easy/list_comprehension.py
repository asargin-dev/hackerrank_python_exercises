import random

x = 3
y = 4
z = 2
n = 3

print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])
