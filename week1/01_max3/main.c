#include <stdio.h>

int main(void)
{
   int a;
   int b;
   int c;
   int max;
   
   printf("세 정수의 최댓값을 구합니다.");   
   printf("정수 a의 값을 입력하세요.\n");
   scanf("%d", &a);
   
   printf("정수 b의 값을 입력하세요\n");
   scanf("%d", &b);
   
   printf("정수 c의 값을 입력하세요\n");
   scanf("%d", &c);

   printf("a: %d, b: %d, c: %d\n",a,b,c);

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

       if(b > c)
       {
           max = c;
       }
   
   }

   printf("최대값은 %d\n",max);

   return 0;
}

