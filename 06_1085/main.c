#include <stdio.h>

int main(void)
{

    int x, y, w, h;
    int route1;
    int route2;
    
    scanf("%d %d %d %d", &x, &y, &w, &h);   


    if(x < w-x)
    {
        route1 = x;
    }
    else
    {    
        route1 = w-x;
    }
    
    if (y < h-y)
    {    
        route2 = y;
    }
    else
    {    
        route2 = h-y;
    }
 
    if(route1<route2)
    {    
        printf("%d\n", route1);
    }
    else
    {    
        printf("%d\n", route2);
    }

    return 0;
}
