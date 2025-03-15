#include <stdio.h>

int main(void)
{
    int a;

    scanf("%d",&a);

    if(a >= 60)
    {
        if(a >= 70)
        {
            if(a >= 80)
            {
                if( a >= 90)
                {
                    printf("A");
                    return 0;
                }
                printf("B");
                return 0;
            }
            printf("C");
            return 0;
        }
        printf("D");
        return 0;            
    }
    else
    {
        printf("F");
    }

    return 0;
}

