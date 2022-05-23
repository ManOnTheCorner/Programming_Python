n = int(input())
m = int(input())
k = int(input())
if n >= m and n >= k and m >= k:
    print(n)
    print(k)
    print(m)
elif m >= n and m >= k and n >= k:
    print(m)
    print(k)
    print(n)
elif m >= n and m >= k and k >= n:
    print(m)
    print(n)
    print(k)
elif n >= m and n >= k and k >= m:
    print(n)
    print(m)
    print(k)
elif k >= n and k >= m and n >= m:
    print(k)
    print(m)
    print(n)
else:
    print(k)
    print(n)
    print(m)