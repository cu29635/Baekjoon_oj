x = int(input())
for i in range(x):
    cnt = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        w = str(i)
        cnt += w.count('0')
    print(cnt)