from bisect import bisect_right, bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m, h = [int(num) for num in input().split()]
    results = [(0, 0) for i in range(n)]
    for i in range(n):
        j = 0
        cur = 0
        problems = 0
        penalty = 0
        t = sorted((int(num) for num in input().split()))
        while j < m and cur + t[j] <= h:
            cur += t[j]
            problems += 1
            penalty -= cur
            j += 1
        results[i] = (problems, penalty)
    rudolf_score = results[0]
    ans = 1
    for i in range(n):
        if results[i] > rudolf_score:
            ans += 1
    print(ans)
    # results.sort()
    # print(results)
    # print(n - bisect_right(results, rudolf_score) + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
