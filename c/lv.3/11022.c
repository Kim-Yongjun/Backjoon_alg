#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d", &a);
    int arr[a];
    int arrB[a];
    int arrC[a];
    for (int i = 0; i < a; i++)
    {
        scanf("%d %d", &b, &c);
        arrB[i] = b;
        arrC[i] = c;
        arr[i] = b + c;
    }
    for (int i = 0; i < a; i++)
    {
        printf("Case #%d: %d + %d = %d\n", i + 1, arrB[i], arrC[i], arr[i]);
    }
    return 0;
}