from collections import Counter


def solution():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    c = Counter()
    for i in range(n):
        c[a[i][0]] += 1

    first = max(c, key=lambda x: c[x])
    second = min(c, key=lambda x: c[x])

    row = 0
    for i in range(n):
        if a[i][0] == second:
            row = i

    ans = [first] + a[row]
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
