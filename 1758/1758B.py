def solution():
    n = int(input())
    if n % 2 == 1:
        ans = (n - 1) * [2] + [2]
    else:
        ans = (n - 2) * [2] + [1, 3]
    for num in ans:
        print(num, end=' ')
    print()


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
