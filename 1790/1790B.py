def solution():
    n, s, r = (int(num) for num in input().split())
    mx = s - r
    n -= 1
    ans = [0] * n
    for i in range(r):
        ans[i % n] += 1
    ans += [mx]
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
