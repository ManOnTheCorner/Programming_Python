a = input()
b = a.upper().count("G")
c = a.upper().count("C")
print((b + c) / len(a) * 100)