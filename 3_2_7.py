"""
Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать. Далее считывает nn строк с числами x_ix
i
​
 , по одному числу в каждой строке. Итого будет n+1n+1 строк.

При считывании числа x_ix
i
​
  программа должна на отдельной строке вывести значение f(x_i)f(x
i
​
 ). Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента xx. Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:

5
5
12
9
20
12
Sample Output:

11
41
47
61
41
"""
n = int(input())
i = 0
d = dict()
for i in range(n):
    x = int(input())
    if x in d:
        print(d[x])
    else:
        d[x] = f(x)
        print(d[x])