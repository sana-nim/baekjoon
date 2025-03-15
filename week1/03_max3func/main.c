#include <stdio.h>

int max3(int a, int b, int c)
{
    int max;
    if(a > b)
    {
        max = a;
        if(a > c)
        {
            max = a;
        }
        else
        {
            max = c;
        }
    }
    else
    {
        max = b;

        if(b>c)
        {
            max = b;
        }
        else
        {
            max = c;
        }
    }
    return max;
}

int main(void)
{
    printf("3,2,1: %d\n", max3(3,2,1));
    printf("3,2,2: %d\n", max3(3,3,2));
    printf("3,1,2: %d\n", max3(3,1,2));
    printf("2,1,3: %d\n", max3(2,3,1));

    return 0;
}
