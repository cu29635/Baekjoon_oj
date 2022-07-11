#include <stdio.h>
int cnt = 0;

void rHanoi(int n, char a, char b, char c){
    if(n==1) printf("%c %c\n", a, c);
    else {
        rHanoi(n-1,a,c,b);
        printf("%c %c\n", a, c);
        rHanoi(n-1,b,a,c);
    }
}
void cntHanoi(int n, char a, char b, char c){
    if(n==1) cnt++;
    else {
        cntHanoi(n-1,a,c,b);
        cnt++;
        cntHanoi(n-1,b,a,c);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    cntHanoi(n, '1', '2','3');
    printf("%d\n", cnt);
    rHanoi(n, '1', '2','3');
    return 0;
}
