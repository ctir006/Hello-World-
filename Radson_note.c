#include <stdio.h>
#include <string.h>

int main()
{
    char a[30000][6],b[30000][6];
    char temp[6];
    int m,n,i,j,f=0;
    scanf("%d%d",&m,&n);
    for(i=0;i<m;i++)
          scanf("%s",a[i]);
    for(i=0;i<n;i++)
          scanf("%s",b[i]);
    if(m<n)
    {
        printf("No");
		return 0;
    }
    else
    {
		int c=1;
        for(i=0;i<n;i++)
        {
			j=0;
			while(j++<m)
			{
				if(strcmp(b[i],a[j])==0)
				{
					c++;
					break;
				}
			}
        }
        if(c==n)
            printf("Yes");
		else
			printf("No");
            
    }
	
    return 0;
}