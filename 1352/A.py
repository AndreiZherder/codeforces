from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    ans = []
    k = 1
    while n:
        while n % 10 == 0:
            n //= 10
            k += 1
        ans.append((n % 10) * 10 ** (k - 1))
        n //= 10
        k += 1
    print(len(ans))
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
