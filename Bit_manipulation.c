#include <stdio.h>

int main()
{
    int n,i;
    int a[100];
	int b[100]={0};
    scanf("%d",&n);
    for(i=1;i<=n;i++)
        scanf("%d",&a[i]);
    for(i=1;i<=n;i++)
    {
        b[a[i]]++;
    }
    for(i=1;i<=100;i++)
    {
		printf("%d\t",b[i]);
        if(b[i]==1)
        {
            printf("%d",i);
            break;
        }
    }
    return 0;
}