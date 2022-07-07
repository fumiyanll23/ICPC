#include <stdio.h>
#include <string.h>

int main(void) {
  int N, i, j;
  int Sum = 0;
  int check_idx = 0;
  int check_len[6] = {5, 12, 17, 24, 31, 31};
  while (1) {
    scanf("%d", &N);
    if (N == 0) {
      break;
    }
    char w[N][10];
    for (j = 0; j < N; j++) {
      scanf("%s", w[i]);
    }
    for (j = 0; j < N; j++) {
      for (i = j; i < N; i++) {
        Sum += strlen(w[i]);
        if (Sum >= check_len[check_idx]) {
          if (Sum == check_len[check_idx]) {
            check_idx++;
            if (Sum == 31) {
              printf("%d\n", j + 1);
              break;
            }
            else {
              break;
            }
          }
        }
      }
      if (Sum == 31) {
        break;
      }
    }
  }
  return 0;
}
