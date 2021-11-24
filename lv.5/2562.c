#include <stdio.h>

int main()
{
    int max = -1000000;
    int count = 0;
    int max_location = 0;

    for (int i = 0; i < 9; i++)
    {
        int k;
        scanf("%d", &k);
        if (k > max)
        {
            max = k;
            max_location = count + 1;
        }
        count++;
    }
    printf("%d\n%d", max, max_location);

    return 0;
}