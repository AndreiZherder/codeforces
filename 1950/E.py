from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
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
    def check(s: str, s1:str) -> bool:
        cnt = 0
        for c1, c2 in zip(s, s1):
            if c1 != c2:
                cnt += 1
                if cnt == 2:
                    return False
        return True

    n = int(input())
    s = input()
    for m in factors(n):
        part = s[:m]
        if check(s, part * (n // m)):
            print(m)
            return
        part = s[m:2 * m]
        if check(s, part * (n // m)):
            print(m)
            return


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
