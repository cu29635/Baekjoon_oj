#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#define getnode() ((node*)malloc(sizeof(node)))
#define MAX_STACK_SIZE 100001
typedef struct q{
    int front;
    int rear;
    int *element;
    int size;
}queue;
void initQueue(queue *q){
    q->front = 0;
    q->rear = q->size - 1;
}
void enqueue(queue *q, int e){
    q->rear = (q->rear+1)%q->size;
    q->element[q->rear] = e;
}
int dequeue(queue *q){
    int e;
    if((q->rear+1)%q->size==q->front){
        return -1;
    }
    e = q->element[q->front];
    q->front = (q->front+1)%q->size;
    return e;
}
int size(queue *q){
    return (q->size-q->front+q->rear+1)%q->size;
}
int front(queue *q){
    if((q->rear+1)%q->size==q->front){
        return -1;
    }
    return q->element[q->front];
}
int back(queue *q){
    if((q->rear+1)%q->size==q->front){
        return -1;
    }
    return q->element[q->rear];
}
void empty(queue *q){
    if((q->rear+1)%q->size==q->front){
        printf("1\n");
    }
    else printf("0\n");
}
int main(){
    int n, m, ele,size_s;
    queue q;
    scanf("%d", &n);
    char arr[21];
    q.element = (int *)malloc(sizeof(int)*n);
    q.size = n;
    initQueue(&q);
    for(int i=0;i<n;i++){
            scanf("%s", arr);
            if(strcmp(arr,"push")==0){
                scanf(" %d", &m);
                enqueue(&q,m);
            }
            else if(strcmp(arr,"pop")==0){
                ele = dequeue(&q);
                printf("%d\n", ele);
            }
            else if(strcmp(arr,"size")==0){
                size_s = size(&q);
                printf("%d\n", size_s);
            }
            else if(strcmp(arr,"empty")==0){
                empty(&q);
            }
            else if(strcmp(arr,"front")==0){
                ele = front(&q);
                printf("%d\n", ele);
            }
            else if(strcmp(arr,"back")==0){
                ele = back(&q);
                printf("%d\n", ele);
            }
        }
    free(q.element);
    return 0;
}
