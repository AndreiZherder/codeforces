from bisect import bisect_right


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    a.sort()
    k = 1
    while k < n + 1:
        i = bisect_right(a, 1)
        if i < k:
            print(k - 1)
            return
        i = bisect_right(a, k)
        if i < 2 * k - 1:
            print(k - 1)
            return
        k += 1
    print(k - 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()