a, b, c = map(int, input().split())

def poww(a,b,c):
    if b == 1 :
        return a%c
    elif b == 2 :
        return (a*a)%c
    else :
        if b%2==0:
            return (poww(a,b//2,c)**2)%c
        else :
            return (poww(a,(b-1)//2,c)**2)*a%c

print(poww(a,b,c))