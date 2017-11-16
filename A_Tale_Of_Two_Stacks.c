#include <stdio.h>

int main()
{
	int n,i,t,p=0,v,q=0,p1=0;
	int a[10000];
	int prin[10000];
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&t);
		if(t==1)
		{
			scanf("%d",&v);
			a[p++]=v;
		}else if(t==2)
		{
			p1++;
		}else
		{
			prin[q++]=a[p1];
		}
	}
	for(i=0;i<q;i++)
		printf("%d\n",prin[i]);
	return 0;
}