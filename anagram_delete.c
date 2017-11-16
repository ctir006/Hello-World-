#include <stdio.h>


int main()
{
    char a[10000],b[10000];
	int i=0,count=0;
	scanf("%s%s",a,b);
	int afreq[150]={0};
	int bfreq[150]={0};
	while(a[i]!='\0')
	{
		afreq[a[i]]++;
		i++;
	}
	i=0;
	while(b[i]!='\0')
	{
		bfreq[b[i]]++;
		i++;
	}
	for(i=97;i<124;i++)
	{
		if(afreq[i]>bfreq[i])
		{
			count=count+(afreq[i]-bfreq[i]);
		}else if(afreq[i]<bfreq[i])
		{
			count=count+(bfreq[i]-afreq[i]);
		}else
		{
			continue;
		}
	}
	printf("%d\n",count);
    return 0;
}