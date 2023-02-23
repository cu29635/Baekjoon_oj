def solution(arr):
    answer = arr[0]
    
    for n in arr:
        answer = answer*n // gcd(answer,n)
    
    return answer

def gcd(a, b):
    while b > 0:
        a, b = b, a % b    
    return a