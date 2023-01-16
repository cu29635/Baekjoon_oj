p = int(input())
m = int(input())
s = input()
arr = "I"
cnt = 0
for _ in range(p):
    arr += "OI"
for i in range(m):
  if s[i:i+len(arr)] == arr :
    cnt += 1
print(cnt)