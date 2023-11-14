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


def prime_factors(n: int):
    """
    Prime factors of n
    prime_factors(99) --> 3 3 11
    """
    while n % 2 == 0:
        yield 2
        n //= 2
    p = 3
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            n = quotient
        else:
            p += 2
    if n != 1:
        yield n


def solution():
    q = int(input())
    pf = list(prime_factors(q))
    if len(pf) <= 1:
        print(1)
        print(0)
    elif len(pf) == 2:
        print(2)
    else:
        print(1)
        print(pf[0] * pf[-1])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
