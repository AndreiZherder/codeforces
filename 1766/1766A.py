def solution():
    n = int(input())
    num = n
    pow = -1
    while num:
        num //= 10
        pow += 1
    ans = 9 * pow + (n // 10 ** pow) % 10
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
