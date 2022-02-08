#include <stdio.h>

int main()
{
    int n, x;
    scanf("%d %d", &n, &x);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        int tmp;
        scanf("%d", &tmp);
        arr[i] = tmp;
    }

    for (int i = 0; i < n; i++)
    {
        if (arr[i] < x)
        {
            printf("%d ", arr[i]);
        }
    }
    printf("\n");
    return 0;
}