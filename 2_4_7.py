s = input()
#s = s.lower()
p = 0
n = len(s)
for i in range(n - 1):
    if s[i] == s[i + 1]:
        p += 1
    if s[i] != s[i + 1]:
        print(s[i], p + 1, end="", sep="")
        p = 0
print(s[-1], p + 1, end="", sep="")