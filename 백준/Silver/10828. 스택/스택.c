#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 10001

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
int size(stack *s){
    return s->top + 1;
}
void IsEmpty(stack *s){
    if(s->top==-1){
        printf("1\n");
    }
    else printf("0\n");
}
void top(stack s){
    if(s.top==-1){
        printf("-1\n");
    }
    else printf("%d\n", s.element[s.top]);
}
int main(){
    int n, m, size_s,ele;
    stack s;
    s.top = -1;
    char arr[21];
    scanf("%d", &n);
    for(int i=0;i<n;i++){
        scanf("%s", arr);
        if(strcmp(arr,"push")==0){
            scanf(" %d", &m);
            push(&s,m);
        }
        else if(strcmp(arr,"pop")==0){
            ele = pop(&s);
            printf("%d\n", ele);
        }
        else if(strcmp(arr,"size")==0){
            size_s = size(&s);
            printf("%d\n", size_s);
        }
        else if(strcmp(arr,"empty")==0){
            IsEmpty(&s);
        }
        else if(strcmp(arr,"top")==0){
            top(s);
        }
    }
    return 0;
}



