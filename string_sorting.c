#include <stdio.h>
#include <string.h>

int main()
{
	int i,j;
	char a[][7]={"give","me","five","know","sanju","chitti"};
	char temp[6];
	for(i=0;i<6;i++)
	{
		printf("%s\t",a[i]);
	}
	printf("\n\n");
	for(i=0;i<6;i++)
	{
		for(j=0;j<5;j++)
		{
			if(strcmp(a[j],a[j+1])>0)
			{
				printf("%s\t%s\n",a[i],a[j]);
				strcpy(temp,a[j+1]);
				strcpy(a[j+1],a[j]);
				strcpy(a[j],temp);
				printf("%s\t%s\n\n",a[i],a[j]);
			}
		}
	}
	for(i=0;i<6;i++)
	{
		printf("%s\t",a[i]);
	}
	return 0;
}