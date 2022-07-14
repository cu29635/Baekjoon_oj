t = int(input())
 
for _ in range(t):
    cntzero = [1,0]
    cntone = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            cntzero.append(cntone[-1])
            cntone.append(cntzero[-2]+cntone[-1]) 
 
    print(cntzero[n], cntone[n])