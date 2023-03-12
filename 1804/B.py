import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k, d, w = [int(num) for num in input().split()]
    ts = [int(num) + w for num in input().split()]
    ans = 0
    cur = [0, 0]
    for t in ts:
        if cur[0] == 0 or cur[1] < t - w:
            ans += 1
            cur = [k, t + d]
        cur[0] -= 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
