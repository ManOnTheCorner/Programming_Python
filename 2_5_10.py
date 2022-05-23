a = [int(i) for i in input().split()]
n = len(a)
if n < 2:
    print(a[0])
else:
    for i in range(n - 1):
        y = a[i - 1]
        x = a[i + 1]
        z = y + x
        print(z, end=" ", sep=" ")
    print(a[-2] + a[0], end=" ", sep=" ")