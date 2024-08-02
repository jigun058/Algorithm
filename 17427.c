#include <stdio.h>

int main() {
    int t, n, i, j;
    scanf("%d", &t);
    
    for (j = 0; j < t; j++) {
        scanf("%d", &n);
        int gN = 0;
        
        for (i = 1; i <= n; i++) {
            gN += i * (n / i);
        }
        
        printf("%d\n", gN);
    }
    
    return 0;
}