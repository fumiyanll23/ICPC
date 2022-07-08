debug_flag = False

while True:
    # input
    n = int(input())
    if n == 0:
        break
    cs = [[*map(int, input().split())] for _ in range(n)]

    # compute
    # 円卓なので2倍の長さで用意する
    finished = [False] * (n * 2)
    p_now = 0
    p_next = 1

    # 初期状態で手札が同じ番号ならばそれらを捨てる
    for i, (c1, c2) in enumerate(cs):
        if c1 == c2:
            finished[i] = True
            finished[i + n] = True

    ans = 0
    while not all(finished):
        # プレイヤーpを求める
        if finished[p_now]:
            for pi, finish in enumerate(finished):
                if not finish:
                    p_now = pi % n
                    break

        if debug_flag:
            print(p_now, finished)
        # プレイヤーp'を求める
        for pj in range(p_now + 1, n * 2):
            if not finished[pj]:
                p_next = pj % n
                if debug_flag:
                    print(f"p_next = {p_next}")
                break

        # プレイヤーp'がpの手札から引く
        card = min(cs[p_now])
        if debug_flag:
            print(cs[p_now], cs[p_next])
        cs[p_next].append(card)
        cs[p_now].remove(card)
        ans += 1
        if debug_flag:
            print(ans, card, cs[p_now], cs[p_next])

        # プレイヤーp'が手札を捨てるかの判定
        for c in cs[p_next][:-1]:
            if c == card:
                # 新たに加えたカード
                cs[p_next].pop()
                # 元からあった手札
                cs[p_next].remove(card)
        if debug_flag:
            print(ans, card, cs[p_now], cs[p_next])

        # プレイヤーp, p'の手札が空であるかの判定
        if len(cs[p_now]) == 0:
            finished[p_now] = True
            finished[p_now + n] = True
        if len(cs[p_next]) == 0:
            finished[p_next] = True
            finished[p_next + n] = True

        p_now = p_next

    # output
    if debug_flag:
        print(f"ans = {ans}")
    print(ans)
