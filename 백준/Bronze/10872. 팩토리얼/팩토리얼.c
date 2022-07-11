#include <stdio.h>

int p(int n){
    if (n==1||n==0) return 1;
    else return n * p(n-1);
}


int main() {
    int n, result=0;
    scanf("%d", &n);
    result = p(n);
    printf("%d",result);
    return 0;
}
