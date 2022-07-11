#include <stdio.h>

int main(){

    int k = 0;
    int result[1000001] = {0,};
    for(int i = 2;i<1000001;i++) {
        if(result[i]==0) {
            for(int j=i*2;j<1000001;j=j+i) result[j] = 1;
        }
    }
    while(1){
        result[1] = 1;
        int n;
        scanf("%d", &n);
        if(n==0) break;
        for(int i = 3;i<n/2+1;i++){
            if(result[i]==0&&result[n-i]==0){
                printf("%d = %d + %d\n", n,i,n-i);
                k = 1;
                break;
            }
        }
        if(k==0) printf("Goldbach's conjecture is wrong.\n");
    }
    
    return 0;
}