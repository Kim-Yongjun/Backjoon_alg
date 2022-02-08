#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d", &a);
    int arr[a];
    for (int i = 0; i < a; i++)
    {
        scanf("%d %d", &b, &c);
        arr[i] = b + c;
    }
    for (int i = 0; i < a; i++)
    {
        printf("Case #%d: %d\n", i + 1, arr[i]);
    }
    return 0;
}