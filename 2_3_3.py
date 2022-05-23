a, b, c, d = int(input()), int(input()), int(input()), int(input())
#a = 7
#b = 10
#c = 5
#d = 6
e = c
z = a
y = c
for i in range((d - c) + 1):
    print("\t", c, end = "")
    c = c + 1
for j in range((b - a) + 1):
    print("\t")
    print(a, end="\t")
    e = y
    for l in range((d - y) + 1):
        print(e * a, end="\t")
        e = e + 1
    a = a + 1