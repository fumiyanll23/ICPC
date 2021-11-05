def main():
    while True:
        # input
        n = int(input())
        if n:
            As = [*map(int, input().split())]
        else:
            return

        # compute

        # output
        print(max(As))


if __name__ == '__main__':
    main()
