#include <stdio.h>
#include <stdlib.h>

long long int gcd(long long int,long long int);
int r[10000][10000]={0};

int main()
{
	long long int n,i,j;
	scanf("%lld",&n);
	long long int a[10000],b[10000];
	for(i=1;i<=n;i++)
		scanf("%lld",&a[i]);
	for(i=1;i<=n;i++)
		scanf("%lld",&b[i]);
	long long int sum=0,cgcd,res=0,res1,prev=0,pres=0;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
            if(r[a[i]][a[j]]>0 || r[a[j]][a[i]]>0)
            {
				if(r[a[i]][a[j]]>0)
					cgcd=r[a[i]][b[j]];
				else
					cgcd=r[a[j]][a[i]];
            }
            else
            {
			    cgcd=gcd(a[i],b[j]);
                r[a[i]][a[j]]=cgcd;
				r[a[j]][a[i]]=cgcd;
            }
			if(cgcd>=sum)
			{
				sum=cgcd;
				res1=a[i]+b[j];
                if(res1>=prev && cgcd>=pres)
                {
					prev=res1;
					pres=cgcd;
                }
			}
		}
	}
	printf("%lld\n",prev);
	return 0;
}

long long int gcd(long long int a,long long int b)
{
	if(b!=0)
		return gcd(b,a%b);
	else
		return a;
}