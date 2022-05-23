n = float(input())
m = float(input())
op = input()
if m == 0 and (op == '/' or op == 'mod' or op == 'div'):
    print("Деление на 0!")
elif op == "-":
    print (n - m)
elif op == "/":
    print(n / m)
elif op == "*":
    print(n * m)
elif op == "mod":
    print(n % m)
elif op == "pow":
    print(n ** m)
elif op == "div":
    print(n // m)
elif op == "+":
    print (n + m)