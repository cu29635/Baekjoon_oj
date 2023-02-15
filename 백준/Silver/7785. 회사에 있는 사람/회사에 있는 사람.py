import sys
input = sys.stdin.readline
n = int(input())
a = dict()
for _ in range(n):
    name, p = map(str, input().split())
    if p =='enter' :
        a[name] = p
    elif p == 'leave' :
        del a[name]
an = sorted(a.keys() , reverse = True)

for k in an:
    print(k)