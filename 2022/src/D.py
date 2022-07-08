while True:
    # input
    n, k = map(int, input().split())
    if n == k == 0:
        break
    ss = [*map(int, input().split())]
    ts = [*map(int, input().split())]
    MOD = 998244353

    # compute
    ans = 0

    # output
    print(ans)
