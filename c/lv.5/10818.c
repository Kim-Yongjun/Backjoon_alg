#include <stdio.h>

int main()
{
    int n;
    int max = -1000000;
    int min = 1000000;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        int k;
        scanf("%d", &k);
        if (k > max)
        {
            max = k;
        }
        if (k < min)
        {
            min = k;
        }
    }
    printf("%d %d", min, max);

    return 0;
}