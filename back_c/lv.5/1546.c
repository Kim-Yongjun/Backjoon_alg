#include <stdio.h>

int main()
{
    int n;
    float max = -1000000;
    float sum;
    scanf("%d", &n);
    float arr[n];
    for (int i = 0; i < n; i++)
    {
        int tmp;
        scanf("%f", &arr[i]);
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    for (int i = 0; i < n; i++)
    {
        arr[i] = (arr[i] / max) * 100;
        sum += arr[i];
    }
    printf("%.6f\n", sum / n);
    return 0;
}