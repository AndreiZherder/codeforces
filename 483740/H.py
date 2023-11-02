from bisect import bisect_right


def solution():
    n = int(input())
    x = sorted([int(num) for num in input().split()])
    q = int(input())
    while q:
        m = int(input())
        print(bisect_right(x, m))
        q -= 1


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
