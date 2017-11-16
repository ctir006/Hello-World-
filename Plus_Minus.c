#include <stdio.h>

int main()
{
	int n,i,a[10000],p=0,ne=0,new=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	for(i=0;i<n;i++)
		if(a[i]==0)
			new++;
		else if(a[i]<0)
			ne++;
		else
			p++;
	printf("%f\n%f\n%f\n",(float)p/n,(float)ne/n,(float)new/n);
	return 0;
}