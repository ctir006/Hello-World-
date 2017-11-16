#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
	struct node *prev;
};

struct node *head=NULL,*curr,*ptr;
void travers(struct node*);

int main()
{
	int num;
	while(1)
	{
		printf("Enter element(enter 0 to exit) :");
		scanf("%d",&num);
		if(num==0)
		{
			printf("Your list elements are : \n");
			travers(head);
		}else
		{
			ptr=(struct node*)malloc(sizeof(struct node));
			ptr->data=num;
			if(head==NULL)
			{
				ptr->next=NULL;
				ptr->prev=NULL;
				head=ptr;
				curr=ptr;
			}else
			{
				ptr->next=NULL;
				ptr->prev=curr;
				curr->next=ptr;
				curr=ptr;
			}	
		}
	}
	return 0;	
}

void travers(struct node *t)
{
		while(t)
		{
			printf("Pre :%d\n",t->data);
			if(t->prev!=NULL)
				printf("Prev : %d\n\n",t->prev->data);
			t=t->next;
		}
}