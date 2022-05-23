a = [int(i) for i in input().split()]
a.sort()
b = []
j = 0
n = len(a)
for i in range(n - 1):
    if a.count(a[i]) > 1 and b.count(a[i]) == 0:
        b.append(a[i])
print(*b)