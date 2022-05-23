a = int(input())
b = int(input())
s = 0
p = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        p += 1
print(s / p)