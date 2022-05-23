a = int(input())
s = []
for i in range(a):
    i += 1
    s.extend([str(i)] * i)
for i in range(a):
    print(s[i], end=" ")