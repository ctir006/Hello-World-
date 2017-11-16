#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char a[20];
    int len;
    char hh[3],mm[3],ss[3];
    scanf("%s",a);
    len=strlen(a);
    if(a[len-2]=='P')
    {
		int i=0,p1=0,p2=0,p3=0;
		while(a[i]!='\0')
		{
			if(i<2 && a[i]!=':')
				hh[p1++]=a[i];
			else if(i<5 && a[i]!=':')
				mm[p2++]=a[i];
			else if(i<8 && a[i]!=':')
				ss[p3++]=a[i];
			i++;	
		}hh[2]='\0';mm[2]='\0';ss[2]='\0';
        if(a[0]=='1'&&a[1]=='2')
	       printf("%d:%s:%s\n",12,mm,ss);
        else    
            printf("%d:%s:%s\n",atoi(hh)+12,mm,ss);
	}else
	{
		int i=0;
		if(a[1]=='2')
		{
			printf("%s","00");
			i=2;
		}
		while(i<strlen(a)-2)
			printf("%c",a[i++]);
		
	}

}
