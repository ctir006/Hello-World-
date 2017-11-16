#include <stdio.h>
#include <stdint.h>

long long int sum(long long int *a,int p)
{
	long long int i,sum=0;
	for(i=0;i<5;i++)
	{
		if(i==p)
			continue;
		else
			sum+=*(a+i);
	}
	return sum;
}

int main()
{
	long long int a[5],i;
	for(i=0;i<5;i++)
		scanf("%lld",&a[i]);
	long long int res[5];
	for(i=0;i<5;i++)
		res[i]=sum(a,i);
	long long int min=INT64_MAX,max=0;
	for(i=0;i<5;i++)
	{
		if(res[i]>max)
			max=res[i];
		if(res[i]<min)
			min=res[i];
	}
	printf("%lld %lld\n",min,max);
	return 0;
}