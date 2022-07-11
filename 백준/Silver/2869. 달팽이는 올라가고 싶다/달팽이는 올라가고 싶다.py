A, B, V = map(int, input().split())
cnt = (V-A)//(A-B)
if((V-A)%(A-B)!=0) : cnt += 1
print(cnt+1)