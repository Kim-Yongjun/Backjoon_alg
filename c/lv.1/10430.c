#include <stdio.h>

int main()
{
    int a, b, c, tmp;
    scanf("%d %d %d", &a, &b, &c);
    tmp = (a + b) % c;
    printf("%d\n", tmp);
    tmp = ((a % c) + (b % c)) % c;
    printf("%d\n", tmp);
    tmp = (a * b) % c;
    printf("%d\n", tmp);
    tmp = ((a % c) * (b % c)) % c;
    printf("%d\n", tmp);

    return 0;
}