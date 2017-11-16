#include <stdio.h>

int fib(int);

int f[100]={0},i;

int main()
{
	int n;
	scanf("%d",&n);
	printf("%d\n",fib(n));
	for(i=0;i<n;i++)
			printf("%d\t",f[i]);
	printf("\n");
	return 0;
}

int fib(int n)
{
		if(n==0)
		{
			return 0;
		}
		else if(n==1)
		{
			f[n]=1;
			return 1;
		}
		else
		{
			if(f[n])
				return f[n];
			else
				f[n]=fib(n-1)+fib(n-2);
		}
		return f[n];
}