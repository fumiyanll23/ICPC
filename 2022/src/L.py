while True:
    # input
    n = int(input())
    if n == 0:
        break
    ws = [input() for _ in range(n)]

    # compute
    check_len = (5, 12, 17, 24, 31, 31)
    for i in range(n):
        len_tanku = 0
        check_idx = 0
        for j in range(i, n):
            len_tanku += len(ws[j])
            if len_tanku >= check_len[check_idx]:
                if len_tanku == check_len[check_idx]:
                    check_idx += 1
                    if len_tanku == 31:
                        print(i + 1)
                        break
                else:
                    break
        if len_tanku == 31:
            break

    # output
