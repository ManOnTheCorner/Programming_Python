a = [int(i) for i in input().split()]
b = int(input())
c = len(a)
d = []
for i in range(c):
    if b == a[i]:
     d.append(i)
    elif not b in a:
        print("Отсутствует")
        break
print(*d)