#include <stdio.h>

int main()
{
    int i,j,c=0,a[600],n,t;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if(a[i]<a[j])
            {
                c++;
                t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
	}printf("\n");
    printf("Array is sorted in %d swaps.\n",c);
    printf("First Element: %d\n",a[0]);
    printf("Last Element: %d\n",a[n-1]);
    return 0;
}