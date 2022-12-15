def solution():
    n = int(input())
    a = [[int(num), i] for i, num in enumerate(input().split())]
    a.sort()
    ans = []
    for i in range(1, n):
        if a[i][0] % a[i - 1][0] != 0:
            x = a[i - 1][0] - (a[i][0] % a[i - 1][0])
            ans.append([a[i][1], x])
            a[i][0] += x
    print(len(ans))
    for i, x in ans:
        print(i + 1, x)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
