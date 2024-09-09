#include<stdio.h>

int main() {
    int K, N, M;
    scanf("%d %d %d", &K, &N, &M);

    int price = K * N;

    if(price <= M){
        printf("%d\n", 0);
    }
    else{
        int a = price - M;
        printf("%d\n", a);
    }

    return 0;
}