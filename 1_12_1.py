x, y, z = int(input()), int(input()), int(input())
p = (x + y + z) / 2
s = (p*(p - x)*(p - y)*(p - z)) ** 0.5
print (s)