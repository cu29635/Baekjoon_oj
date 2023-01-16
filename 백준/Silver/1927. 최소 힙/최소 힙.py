import heapq
import sys
 
n = int(sys.stdin.readline())
heap = list()
for _ in range(n):
    k = int(sys.stdin.readline())
    if k==0 :
        if not heap:
            print("0")
        else :
            print(heapq.heappop(heap))
    else :
        heapq.heappush(heap,k)