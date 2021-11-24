#include <stdio.h>

int main()
{
    int a, count, tmp;
    count = 0;
    int i, j, k, r;

    scanf("%d", &a);
    tmp = a;
    while (1)
    {
        i = tmp / 10;
        j = tmp % 10;
        k = (i + j) % 10;
        r = j * 10 + k;
        count++;
        if (r == a)
        {
            break;
        }
        tmp = r;
        }
    printf("%d\n", count);
    return 0;
}