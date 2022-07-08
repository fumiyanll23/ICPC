#include<stdio.h>

int main() {
  int n, i;
  int Cou;

  while(1) {
    // input
    scanf("%d", &n);
    if (n == 0) {
      break;
    }
    int v[n];
    for (i = 0; i < n; i++) {
      scanf("%d", &v[i]);
    }

    // compute
    Cou = 0;
    for (i = 1; i < n - 1; i++) {
      if (v[i] > v[i-1] && v[i] > v[i+1]) {
        Cou++;
      }
    }

    // output
    printf("%d\n", Cou);
  }
  return 0;
}
