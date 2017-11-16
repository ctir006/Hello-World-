#include <stdio.h>

int main()
{
	long long int n,m,r;
	scanf("%lld",&m);
	int f=0,b=0,i=0,k,p=0;
	for(n=m+1;n<=999999;n++)
	{
		r=n;f=0;b=0;i=0;
		while(r>0)
		{
				if(i<=2)
				{
					k=r%10;
					b+=k;
					i++;
				}else
				{
					k=r%10;
					f+=k;
					i++;
				}
				r=r/10;
		}
		if(f==b)
		{
			p=1;
			printf("%lld\n",n);
		}
		if(p==1)
			break;
	}
	return 0;
}