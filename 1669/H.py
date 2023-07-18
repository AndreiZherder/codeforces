from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    c = Counter({j: 0 for j in range(31)})
    for j in range(31):
        mask = 1 << j
        for num in a:
            if num & mask == 0:
                c[j] += 1
    ans = 0
    for j, cnt in sorted(c.items(), reverse=True):
        if cnt <= k:
            k -= cnt
            ans |= 1 << j
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
