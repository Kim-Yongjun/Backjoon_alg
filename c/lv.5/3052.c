#include <stdio.h>

int main()
{
    int arr[10];
    int count = 0;
    int result = 0;

    for (int i = 0; i < 10; i++)
    {
        int tmp;
        scanf("%d", &tmp);
        arr[i] = tmp % 42;
    }

    for (int j = 0; j < 10; j++)
    {
        count = 0;
        for (int k = j + 1; k < 10; k++)
        {
            if (arr[j] == arr[k])
            {
                count += 1;
            }
        }
        if (count == 0)
        {
            result += 1;
        }
    }
    printf("%d\n", result);

    return 0;
}