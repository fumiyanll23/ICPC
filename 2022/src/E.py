while True:
    # input
    n, m = map(int, input().split())
    if n == m == 0:
        break
    As = input().split()
    Bs = input().split()
    print(As)
    print(Bs)

    # compute
    flag = True

    # 交差点を初期化する
    anss = ["-" * m for _ in range(n)]
    for i, A in enumerate(As):
        print(i, A)
        if A == "1":
            anss[i][0] = "+"
    for j, B in enumerate(Bs):
        if B == "1":
            anss[0][j] = "+"

    # output
    if flag:
        print("Yes")
        for ans in anss:
            print(ans)
    else:
        print("No")
