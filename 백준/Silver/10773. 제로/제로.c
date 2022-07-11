#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 100001

typedef struct st{
    int element[MAX_STACK_SIZE];
    int top;
}stack;
void push(stack *s, int e){
    s->top++;
    s->element[s->top] = e;
}
int pop(stack *s){
    int e = 0;
    if(s->top == -1){
        return -1;
    }
    e = s->element[s->top];
    s->top--;
    return e;
}

int main(){
    int k, n, sum = 0, e;
    stack s;
    s.top = -1;
    scanf("%d", &k);
    for(int i=0;i<k;i++){
        scanf("%d", &n);
        if(n==0){
            e = pop(&s);
            sum = sum - e;
        }
        else{
            push(&s,n);
            sum = sum + n;
        }
    }
    printf("%d", sum);
    return 0;
}
