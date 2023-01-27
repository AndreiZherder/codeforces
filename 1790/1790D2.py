from collections import Counter


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    c = Counter(a)
    h = [[k, v] for k, v in sorted(c.items())]
    n = len(h)
    ans = 0
    start = 0
    while start < n:
        i = start
        h[i][1] -= 1
        i += 1
        while i < n and h[i][0] == h[i - 1][0] + 1 and h[i][1] > 0:
            h[i][1] -= 1
            i += 1
        ans += 1
        while start < n and h[start][1] == 0:
            start += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()