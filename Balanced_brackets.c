#include <stdio.h>
#include <string.h>

int main()
{
	int i,n,j,k,l=0;
	char a[1000][1001];
	char c[]={'{','[','('};
	char d[]={'}',']',')'};
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%s",a[i]);
	for(i=0;i<n;i++)
	{
		char t[1001];
		int p=0,f=0;
		char r[1001];
		strcpy(r,a[i]);
		j=0;
		while(r[j]!='\0')
		{
			for(k=0;k<3;k++)
			{
				if(r[j]==c[k])
				{
					t[p++]=r[j];
					break;
				}
				if(r[j]==d[k])
				{
					if(r[j]==41)
					{
						if(t[--p]==40)
						{
							t[p]='\0';
						}
						else
						{
							printf("NO\n");
							f=1;
							break;
						}
					}
					if(r[j]==93)
					{
						if(t[--p]==91)
						{
							t[p]='\0';
						}
						else
						{
							printf("NO\n");
							f=1;
							break;
						}
					}
					if(r[j]==125)
					{
						if(t[--p]==123)
						{
							t[p]='\0';
						}
						else
						{
							printf("NO\n");
							f=1;
							break;
						}
					}
				}
			}
			if(f==1)
			{
				break;
			}
			j++;
			if(r[j]=='\0')
				if(p==0)
					printf("YES\n");
				else
					printf("NO\n");
		}
	}
	return 0;
}