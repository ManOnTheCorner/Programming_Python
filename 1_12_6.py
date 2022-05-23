n = int(input())
if n > 100 and (n % 100) // 10 == 1:
    print(n, ' программистов', sep='')
elif n == 1:
    print(n, ' программист', sep='')
elif n > 20 and n % 10 == 1:
    print(n, ' программист', sep='')
elif n > 20 and (n == 2 or n == 3 or n == 4 or n % 10 == 2 or n % 10 == 3 or n % 10 == 4):
    print(n, ' программиста', sep='')
elif n == 2 or n == 3 or n == 4:
    print(n, ' программиста', sep='')
else:
    print(n, ' программистов', sep='')