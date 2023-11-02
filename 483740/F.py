def solution():
    n, m, x = [int(num) for num in input().split()]
    x -= 1
    j = x // n
    i = x % n
    print(i * m + j + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
