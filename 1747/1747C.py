def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if a[0] == 1:
        print('Bob')
        return
    if any(a[i] == 1 for i in range(1, n)):
        print('Alice')
        return
    if (sum(a) - n * 2) % 2 == 1:
        print('Alice')
    else:
        print('Bob')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
