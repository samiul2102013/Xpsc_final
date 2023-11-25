#include <stdio.h>
#include <string.h>

int main() {
    char a[11], b[11];
    scanf("%s", a);
    scanf("%s", b);

    int m = strlen(a);
    int n = strlen(b);
    printf("%d %d\n", m, n);
    
    char c[m + n + 1];
    strcpy(c, a);
    strcat(c, b);

    printf("%s\n", c);

    int temp = a[0];
    a[0] = b[0];
    b[0] = temp;
    printf("%s %s\n", a, b);

    return 0;
}
