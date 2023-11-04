#include <stdio.h>
#include<stdlib.h>
void fun(int a , int b, float *sum, float *prd, float *ag);
int main(){
    int *ptr,a;
    ptr = (int*) malloc(5*sizeof(int));
   
}

void fun(int a , int b, float *sum, float *prd, float *ag){
    *sum = a+b;
    *prd = a*b;
    *ag = (*sum)/2;
}