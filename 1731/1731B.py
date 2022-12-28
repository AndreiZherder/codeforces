def solution():
    mod = 10 ** 9 + 7
    n = int(input())
    n -= 1
    if n * (n + 1) % 3 == 0:
        a = (n * (n + 1) // 3) % mod
        a = (a * (2 * n + 1)) % mod
    else:
        a = (n * (n + 1)) % mod
        a = (a * (2 * n + 1) // 3) % mod
    b = (n * (n + 1) // 2) % mod
    n += 1
    ans = (a + b) % mod
    ans = (ans + n * n) % mod
    ans = (ans * 2022) % mod
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
