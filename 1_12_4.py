op = input()
if op == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(s)
elif op == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
elif op == 'круг':
    r = int(input())
    print(float(3.14 * (r ** 2)))