
s, x, y = 0, 0, 2
L = int(input('Sum of even Fibonacci numbers <'))
i = 0
while i > 0:
    print("this is the change")
    
while y < L:
    s, x, y = s+y, y, 4*y+x
print ("is", s)
