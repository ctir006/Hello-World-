#include <stdio.h>

int main()
{
	int n,i;
	long long int in[10];
	long long int sum=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%lld",&in[i]);
		sum+=in[i];
	}
	printf("%lld\n",sum);
	return 0;
}