#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	unsigned long long int n,i,c=0,j,l,k;
	char a[][2][22]=malloc(sizeof(int)*90100);
	char names[10000][22];
	char par[22],t[22];
	scanf("%llu",&n);
	for(i=0;i<n;i++)
		scanf("%s%s",a[i][1],a[i][2]);
	for(i=0;i<n;i++)
	{
		if(strcmp(a[i][1],"add")==0)
			strcpy(names[c++],a[i][2]);
		if(strcmp(a[i][1],"find")==0)
		{
			unsigned long long int f=0,count=0;
			strcpy(par,a[i][2]);
			for(j=0;j<c;j++)
			{
				f=0;
				for(k=0;k<strlen(names[j]);k++)
				{
					if(names[j][k]==par[0])
					{
						for(l=0;l<strlen(par);l++)
						{
							if(names[j][k+l]==par[l])
							{
								f++;
							}
							else
							{
								f=0;
								break;
							}								
						}
						if(f==strlen(par))
							count++;
					}
				}
			}
			printf("%llu\n",count);
		}
	}
	return 0;
}