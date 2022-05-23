a = int(input())
s = 0
q = 0
s += a
q += a * a
while s != 0:
    a = int(input())
    s += a
    q += a * a
print (q)