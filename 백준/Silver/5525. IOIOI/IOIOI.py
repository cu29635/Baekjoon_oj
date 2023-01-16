import sys

p = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()
arr = "I"
cnt = 0
for _ in range(p):
    arr += "OI"
for i in range(m):
  if s[i:i+len(arr)] == arr :
    cnt += 1
print(cnt)