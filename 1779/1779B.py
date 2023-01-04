def solution():
    n = int(input())
    if n % 2 == 1:
        if n == 3:
            print('NO')
        else:
            print('YES')
            b = n // 2
            a = -(b - 1)
            for i in range(n // 2):
                print(a, b, end=' ')
            print(a)
    else:
        print('YES')
        for i in range(n // 2):
            print(-1, 1, end=' ')
        print()


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
