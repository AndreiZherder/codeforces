from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def factors(n: int):
    """
    Distinct factors of n
    """
    stack = []
    yield 1
    if n != 1:
        stack.append(n)
    p = 2
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            if quotient != p:
                stack.append(quotient)
        p += 1
    while stack:
        yield stack.pop()


def solution():
    n = int(input())
    nums = input().split()
    c = Counter()
    for num in nums:
        if int(num) <= n:
            c[num] += 1
    if not c:
        print(0)
        return
    best = 0
    mn = min(int(num) for num in c)
    for i in range(mn, n + 1):
        cur = sum(c[str(f)] for f in factors(i))
        best = max(best, cur)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
