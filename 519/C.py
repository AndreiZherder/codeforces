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


def solution():
    n, m = [int(num) for num in input().split()]
    if m > n:
        n, m = m, n
    ans = 0
    while n >= 2:
        if m > 0:
            ans += 1
            n -= 2
            m -= 1
            if m > n:
                n, m = m, n
        else:
            break
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
