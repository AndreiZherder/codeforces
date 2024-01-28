from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


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
    x, n = [int(num) for num in input().split()]
    ans = 1
    for f in factors(x):
        if x >= f * n:
            ans = f
        else:
            break
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
