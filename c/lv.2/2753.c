#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    if (a >= 1 && b < 45)
    {
        printf("%d %d", a - 1, b + 15);
    }
    else if (a < 1 && b < 45)
    {
        printf("%d %d", 24 - 1, b + 15);
    }
    else
    {
        printf("%d %d", a, b - 45);
    }
    return 0;
}