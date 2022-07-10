while True:
    # input
    n = int(input())
    if n == 0:
        break
    vs = [*map(int, input().split())]

    # compute
    ans = 0
    for v0, v1, v2 in zip(vs, vs[1:], vs[2:]):
        if v0 < v1 and v1 > v2:
            ans += 1

    # output
    print(ans)
