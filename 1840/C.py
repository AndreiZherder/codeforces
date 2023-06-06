import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k, q = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    ans = 0
    segments = []
    i = 0
    while i < n:
        while i < n and a[i] > q:
            i += 1
        j = i + 1
        while j < n and a[j] <= q:
            j += 1
        if i < n and j - i >= k:
            segments.append([i, j - 1])
        i = j
    for i, j in segments:
        n = j - i + 1
        ans += (1 + n - k + 1) * (n - k + 1) // 2
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
