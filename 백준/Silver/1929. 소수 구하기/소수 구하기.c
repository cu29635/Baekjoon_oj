#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int n, m;
    int result[1000001] = {0,};
    scanf("%d %d", &m,&n);
    result[1] = 1;
    for(int i = 2;i<n+1;i++) {
        if(result[i]==0) {
            if(i>=m) printf("%d\n", i);
            
            for(int j=i*2;j<n+1;j=j+i) if(result[j]==0) result[j] = 1;
        }
    }
    return 0;
}
