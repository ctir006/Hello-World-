#include <stdio.h>
#include <stdint.h>
#include <math.h>

int McM(int max[][6],int *a,int i,int j)
{
	int q,k;
	if(max[i][j]<INT32_MAX)
		return max[i][j];
	if(i==j)
	{
		return 0;
	}
	else
	{
		for(k=i;k<=j-1;k++)
			q=McM(max,a,i,k)+McM(max,a,k+1,j)+a[i-1]*a[k]*a[j];
		if(q<max[i][j])
			max[i][j]=q;
	}
	return max[i][j];
}

int main()
{
	int max[6][6]={0};
	int i,j;
	int a[]={1,2,3,4,5};
	for(i=1;i<=5;i++)
		for(j=1;j<=5;j++)
			max[i][j]=INT32_MAX;
	printf("Max Number of Multiplications : %d",McM(max,a,1,4));
}