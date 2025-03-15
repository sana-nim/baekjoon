#include <stdio.h>

int main(void)
{
    char name[100];
    printf("이름을 입력하세요\n");
    scanf("%s",name);
    

    printf("안녕하세요! 제 이름은 %s입니다",name);

    return 0;
}

