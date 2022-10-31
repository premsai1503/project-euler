
s, x, y = 0, 0, 2
L = int(input('Sum of even Fibonacci numbers <'))
while y < L:
    s, x, y = s+y, y, 4*y+x
print ("is", s)
