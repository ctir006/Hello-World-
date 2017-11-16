#include <stdio.h>
#include <stdlib.h>

int main()
{
	return 0;
}


bool has_cycle(Node* head) {
    struct node *a[100]={null};
    struct node *t;
    int i=0,c=0;
    t=head;
    while(t!=null)
    {
        a[i++]=t;
		t=t->next;
		c++;
    }
    for(i=0;i<c;i++)
	{
		for(j=i;j<c;j++)
		{
			if(a[i]==a[j])
				return 0;
		}
		return 1;
	}
}