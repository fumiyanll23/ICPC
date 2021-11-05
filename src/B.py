def main():
    # input
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            return
        else:
            k = w + h - 1
            xyns = []
            for _ in range(k):
                x, y, n = map(int, input().split())
                xyns.append([x-1, y-1, n])

        # compute
        cols = [0] * w
        rows = [0] * h
        xys = []
        for x, y, _ in xyns:
            xys.append([x, y])
        ## 左端は必ず0が入る
        si = 0
        cols[si] = 1

        ## 行と列を交互に調べる
        for k in range(w*h):
            for hj in range(h):
                if [si, hj] in xys:
                    rows[hj] = 1
                    xys.remove([si, hj])
            if k == 0:
                sj = min(hj for hj in range(h) if rows[hj] == 1)
            else:
                for j in range(sj+1, h):
                    if rows[j]:
                        sj = j
                        break
            for wi in range(w):
                if [wi, sj] in xys:
                    cols[wi] = 1
                    xys.remove([wi, sj])
            for i in range(si+1, w):
                if cols[i]:
                    si = i
                    break

        # output
        if sum(cols) == w and sum(rows) == h:
            print('YES')
        else:
            print('NO')
        print(xys)
        print(cols)
        print(rows)


if __name__ == '__main__':
    main()
