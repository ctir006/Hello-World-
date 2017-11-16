#include <stdio.h>

int main()
{
	int n,i,j;
	scanf("%d",&n);
	int in[100][100];
	int d1=0,d2=0;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&in[i][j]);
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(i==j)
				d1+=in[i][j];
		}
	}
	int p1=n-1,p2=0;
	while(p1>=0)
	{
		d2+=in[p1--][p2++];
	}
    int res;
    res=d2-d1;
    if(res<0)
        printf("%d\n",-1*res);
    else
	   printf("%d\n",res);
	return 0;
}