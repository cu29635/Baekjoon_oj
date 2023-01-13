n = int(input())
d = dict()
s = list()
for _ in range(n):
    x, y = map(str, input().split())
    d[y] = x
    s.append(y)
arr = input()
for st in s:
    arr = arr.replace(st, d[st])
a, b = map(int, input().split())
print(arr[a-1:b])