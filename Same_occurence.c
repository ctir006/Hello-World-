#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n,i,j,k;
	long long int q;
	long long int a[80],x,y;
	scanf("%d%lld",&n,&q);
	for(i=0;i<n;i++)
		scanf("%lld",&a[i]);
	scanf("%lld%lld",&x,&y);
	int t[80][80]={0};
	int res=0;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(j<i)
				continue;
			int c1=0,c2=0;
			for(k=i;k<=j;k++)
			{
				if(a[k]==x)
					c1++;
				if(a[k]==y)
					c2++;
			}
			if(c1==c2)
				res++;
		}
	}
	printf("%d\n",res);
	return 0;
}