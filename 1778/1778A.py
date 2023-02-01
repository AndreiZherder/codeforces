def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    for i in range(1, n):
        if a[i] == a[i - 1] and a[i] == -1:
            print(sum(a) + 4)
            return
    if -1 in a:
        print(sum(a))
    else:
        print(sum(a) - 4)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
