def solution():
    n = int(input())
    if n <= 3:
        ans = list(range(1, n + 1))
    else:
        ans = []
        add = []
        if n % 2 == 0:
            j = n // 2
            i = n
        else:
            j = n // 2
            i = n - 1
            add = [n]
        while j > 0:
            ans.append(j)
            ans.append(i)
            j -= 1
            i -= 1
        ans += add
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
