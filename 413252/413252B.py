def solution():
    s = input()
    n = len(s)
    if s[:n // 2] == s[n //2: n]:
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
