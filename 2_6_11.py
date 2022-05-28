""""
Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n
2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

a = int(input())
b = [[0] * a for i in range(a)]
count = 0
for j in range(a):
    count += 1
    b[0][j] = count
i = 0
j = a - 1
a -= 1
while len (b) ** 2 != count:
    for k in range(a):
        i += 1
        count += 1
        b[i][j] = count
    for k in range(a):
        j -= 1
        count += 1
        b[i][j] = count
    for k in range(a-1):
        i -= 1
        count += 1
        b[i][j] = count
    for k in range(a-1):
        j += 1
        count += 1
        b[i][j] = count
    a -= 2
for i in range(len(b)):
    for j in range (len(b[j])):
        print(b[i][j], end=' ')
    print()