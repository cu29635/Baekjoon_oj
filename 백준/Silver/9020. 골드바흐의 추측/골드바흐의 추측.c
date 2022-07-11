#include <stdio.h>

int main(){

    int k = 0;
    int x = 0, y = 0;
    int result[1000001] = {0,};
    for(int i = 2;i<1000001;i++) {
        if(result[i]==0) {
            for(int j=i*2;j<1000001;j=j+i) result[j] = 1;
        }
    }
    scanf("%d", &k);
    for(int j=0;j<k;j++){
        result[1] = 1;
        int n;
        scanf("%d", &n);
        if(n==0) break;
        for(int i = 2;i<n/2+1;i++){
            if(result[i]==0&&result[n-i]==0){
                x = i;
                y = n-i;
            }
        }
        printf("%d %d\n", x,y);
    }
    return 0;
}