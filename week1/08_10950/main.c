#include <stdio.h>
int main(void)
{
    int repeat, input1, input2,i;
    scanf("%d",&repeat);
    for(i = 0; i < repeat; i++)
    {
        scanf("%d %d", &input1, &input2);
        printf("%d\n", input1+input2);
    }

    return 0;
}
