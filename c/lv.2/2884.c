#include <stdio.h>

int main()
{
    int a, tmp1, tmp2, tmp3;
    scanf("%d", &a);
    tmp1 = a % 4;
    tmp2 = a % 100;
    tmp3 = a % 400;

    if (tmp1 == 0 && tmp2 != 0)
    {
        printf("1\n");
    }
    else if (tmp3 == 0)
    {
        printf("1\n");
    }
    else
    {
        printf("0\n");
    }
    return 0;
}