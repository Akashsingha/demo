/* Write A program in C to --
1. Insert An Element in a Position of an array taken by user.
2. Delete An Element from any Position of an array on c of user.
3. Display The Final Integer Array*/

#include <stdio.h>
#include <stdbool.h>
int arr[50], n; // Array and size of array (n) initialise as a global Variable.

void Display()
{

    printf("Displaying the Array:\n\n");
    for (int i = 0; i < n; i++)
    {
        printf("Element index [%d]\t", i);
        printf("%d\n", arr[i]);
    }
}

void Insert(int num, int pos)
{

    for (int i = n+1; i > pos; i--)
    {
        arr[i] = arr[i-1];
    }
    arr[pos] = num;
    Display();
    printf("Succesfully inserted");
}

void Delete(int num)
{
    bool Flag = false;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == num) Flag = true;
        if(Flag==true)
        {
            arr[i] = arr[i + 1];
        }
    }
    Display();
}

int main()
{

    int x, num, pos;

    printf("Enter the size of array\n");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("Enter the element at index [%d]: ", i);
        scanf("%d", &arr[i]);
    }

    do
    {
        printf("\n\nChoose one of this:\n");
        printf("1. Insert An Element in a Position\n2. Delete An Element from any Position\n3. Display the array\n4. Exit\n");
        scanf("%d", &x);
        switch (x)
        {
        case 1:
            printf("Enter the number you want to Insert\t");
            scanf("%d", &num);
            printf("In which position you want to Insert\t");
            scanf("%d", &pos);

            Insert(num, pos);

            break;
        case 2:
            printf("Enter the number you want to Delete\t");
            scanf("%d", &num);

            Delete(num);
            break;
        case 3:
            Display();
            break;
        }
    } while (x != 4);
}