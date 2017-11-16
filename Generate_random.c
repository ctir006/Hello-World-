#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int random_number();

int main()
{
	int n,c=0,alpha,special,number;
	scanf("%d",&n);
	alpha=random_number()%26;
	special=random_number()%25;
	number=random_number()%10;
	printf("%d\t%d\t%d\n",alpha,special,number);
	while(c<n)
	{
		if((97+alpha)<122)
		{
			printf("%c\n",97+alpha++);
		}
		else
		{
			alpha=0;
			printf("%c\n",97+alpha++);
		}
		c++;
		if((33+special)<48)
		{
			printf("%c\n",33+special++);
		}
		else
		{
			special=0;
			printf("%c\n",33+special++);
		}
		c++;
		if((48+number)<57)
		{
			printf("%c\n",48+number++);
		}
		else
		{
			number=0;
			printf("%c\n",48+number++);
		}
		c++;
	}
	printf("\n");
	return 0;
}

int random_number()
{
    srand(time(NULL));
    return rand();
}