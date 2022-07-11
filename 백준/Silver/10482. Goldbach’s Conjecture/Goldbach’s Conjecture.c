#include <stdio.h>

int main(){
    int k = 0;
    int result[1000001] = {0,};
    result[1] = 1;
    for(int i = 2;i<1000001;i++) {
        if(result[i]==0) {
            for(int j=i*2;j<1000001;j=j+i) result[j] = 1;
        }
    }
    scanf("%d", &k);
    for(int j=0;j<k;j++){
        int n;
        int cnt=0;
        scanf("%d", &n);
        if(n==0) break;
        for(int i = 2;i<n/2+1;i++){
            if(result[i]==0&&result[n-i]==0){
                cnt++;
            }
        }
        printf("%d has %d representation(s)\n", n, cnt);
        for(int i = 2;i<n/2+1;i++){
            if(result[i]==0&&result[n-i]==0){
                printf("%d+%d\n", i, n-i);
            }
        }
        printf("\n");
    }
    return 0;
}