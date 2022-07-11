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
    while(1){
        int n;
        int cnt=0;
        scanf("%d", &n);
        if(n==0) break;
        for(int i = 3;i<n/2+1;i++){
            if(result[i]==0&&result[n-i]==0){
                cnt++;
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}