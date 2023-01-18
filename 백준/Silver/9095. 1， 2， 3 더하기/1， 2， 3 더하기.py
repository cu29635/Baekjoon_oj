def solution(n):
    table = dict() 
    table[0], table[1], table[2] = 1,1,2
    for i in range(3,n+1):
        table[i] = table[i-1] + table[i-2] + table[i-3]

    return table[n]

N = int(input())

for i in range(N):
    k = int(input())
    print(solution(k))