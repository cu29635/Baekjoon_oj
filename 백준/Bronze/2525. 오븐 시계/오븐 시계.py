x, y = map(int, input().split())
t = int(input())

x += t//60
y += t%60

if y >= 60:
    x += 1
    y -= 60
if x >= 24:
    x -= 24

print(x, y)