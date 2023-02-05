def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    a.sort()
    ans = 0
    i = 0
    for j in range(n):
        if a[j] > i:
            i += 1
            ans += a[j] - i

    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
