#include <stdio.h>

int main()
{
    int a, b;
    int tmp1, tmp2, tmp3;

    scanf("%d\n%d", &a, &b);

    tmp1 = b / 100;
    tmp2 = (b % 100) / 10;
    tmp3 = ((b % 100) % 10);
    printf("%d\n", a * tmp3);
    printf("%d\n", a * tmp2);
    printf("%d\n", a * tmp1);
    printf("%d\n", a * b);

    return 0;
}