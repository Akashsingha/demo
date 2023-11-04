#include <stdio.h>
#include <stdlib.h>

struct node
{
    int Data;
    struct node *next;
};

void Traversal(struct node *ptr)
{

    while (ptr != NULL)
    {
        printf("%d\t", ptr->Data);
        ptr = ptr->next;
    }
    printf("\n");
}

struct node *Insert_at_begining(struct node *head, int value)
{
    struct node *ptr;
    ptr = (struct node *)malloc(sizeof(struct node));
    ptr->Data = value;

    ptr->next = head;
    head = ptr;

    return ptr;
}
struct node *Insert_at_End(struct node *head, int value)
{
    struct node *ptr, *p;
    ptr = (struct node *)malloc(sizeof(struct node));
    p = (struct node *)malloc(sizeof(struct node));

    ptr->Data = value;

    p = head;

    for (int i = 0; p->next != NULL; i++)
    {
        p = p->next;
        printf("%d : %d\t",i, p->Data);
        
    }

    printf("here");
    ptr->next = p->next;
    printf("%d %d", ptr->Data, p->Data);
    p->next = ptr;
    return head;
}
int main()
{
    struct node *head;
    struct node *first;
    struct node *second;
    struct node *third;

    head = (struct node *)malloc(sizeof(struct node));
    first = (struct node *)malloc(sizeof(struct node));
    second = (struct node *)malloc(sizeof(struct node));
    third = (struct node *)malloc(sizeof(struct node));

    head->Data = 1;
    head->next = first;
    first->Data = 2;
    first->next = second;
    second->Data = 3;
    second->next = third;
    third->Data = 4;
    third->next = NULL;

    Traversal(head);
    // head = Insert_at_begining(head, 45);
    // Traversal(head);
    head = Insert_at_End(head, 78);
    Traversal(head);
}