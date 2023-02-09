a = input()
lis = list()
for k in a:
    lis.append(int(k))
lis.sort()
lis.reverse()
n = ''
for i in lis:
    n = n + str(i)
print(n)