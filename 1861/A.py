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


def is_prime(n: int):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    # all primes > 3 are of the form 6n ± 1
    p = 5
    while p * p <= n:
        if n % p == 0:
            return False
        if n % (p + 2) == 0:
            return False
        p += 6
    return True


def solution():
    s = input()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            x = int(s[i]) * 10 + int(s[j])
            if is_prime(x):
                print(x)
                return
    print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
