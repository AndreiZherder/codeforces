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


mod = 10 ** 9 + 7
factorials = [1]
def fac(n, cache=True):
    """
    returns n!
    """
    if not cache:
        ans = 1
        for i in range(1, n + 1):
            ans = (ans * i) % mod
        return ans
    else:
        while len(factorials) < n + 1:
            factorials.append((factorials[-1] * len(factorials)) % mod)
        return factorials[n]


def solution():
    n = int(input())
    print((fac(n, False) - pow(2, n - 1, mod)) % mod)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
