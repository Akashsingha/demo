/* Write A program in C to take 2 Sparse Matrix and firstly convert 
them in 3-tuple form and then add them to get the final output as the 
sparse matrix */

#include<stdio.h>
int arr[3][3];

int SparseMatrix(){
    printf("Enter the number in Sparse matrix:\n");

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%d",&arr[i][j]);
        }
        // printf("\nNext row\n");
    }
    return arr[3][3];
}

void Display(int arr[3][3]){
    for (int i = 0; i < 3; i++)
    {
        printf("[");
        for (int j = 0; j < 3; j++)
        {
            printf("%d  ",&arr[i][j]);
        }
        printf("]\n");
    }
    
}

int main()
{

    printf("Fill the First matrix:\n");
    
    Display(SparseMatrix());
}