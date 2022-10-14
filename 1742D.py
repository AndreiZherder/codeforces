from math import gcd


def solution():
    n = int(input())
    a = list(map(int, input().split()))
    ans = -1
    d = [0 for i in range(1000)]
    for i in range(n):
        d[a[i] - 1] = i
    for i in range(1000):
        for j in range(i, 1000):
            if gcd(a[d[i]], a[d[j]]) == 1:
                ans = max(ans, d[i] + d[j] + 2)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
