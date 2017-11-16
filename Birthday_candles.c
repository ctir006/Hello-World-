#include <stdio.h>

int main()
{
	long long int n,i,j,temp;
	scanf("%lld",&n);
	long long int a[100000];
	for(i=0;i<n;i++)
		scanf("%lld",&a[i]);
	for(i=1;i<n;i++)
	{
		for(j=0;j<n-i;j++)
		{
			if(a[j]<a[j+1])
			{
				temp=a[j+1];
				a[j+1]=a[j];
				a[j]=temp;
			}
		}
	}
	long long int c=0,v;
	for(i=0;i<n;i++)
	{
		if(c==0)
			v=a[i];
		if(a[i]==v)
			c++;
		else
			break;
	}
	printf("%lld\t",c);
	return 0;
}