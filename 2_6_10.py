a = []
b = 0
i = 0
j = 0
z = 0
while True:
    text = input()
    if text == 'end':
        break
    a.append(list(map(int, text.split())))
n = len(a)
m = len(a[i])
for i in range(n):
    for j in range(m):
        b = a[i-n+1][j] + a[i-1][j] + a[i][j-m+1] + a[i][j-1]
        print(b, end=' ')
    print()