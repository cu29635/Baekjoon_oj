def fibonacci(n):
  d[0] = 0
  d[1] = 1

  if(n<2):
    return d[n]

  for i in range(2,n+1):
    d[i] = d[i-2] + d[i-1]

  return d[n]

if __name__ == '__main__':
  n = int(input())
  d = [0 for i in range(100000)]
  print(fibonacci(n))