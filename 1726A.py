
def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if n == 1:
        print(0)
        return
    d1 = max(a[1:]) - a[0]
    d2 = a[n - 1] - min(a[:n - 1])
    ans = max(d1, d2)
    for i in range(1, n):
        ans = max(ans, a[i - 1] - a[i])
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
