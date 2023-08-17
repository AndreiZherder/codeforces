from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    m, k, a1, ak = [int(num) for num in input().split()]
    INF = 10 ** 20
    y = a1 + min(m // k, ak) * k
    if y >= m:
        print(0)
        return
    z = m - (m - y) // k * k
    if z - k < 0:
        print(z - y + (m - z) // k)
    elif a1 < y - (z - k):
        print(z - y + (m - z) // k)
    else:
        print(min((m - (z - k)) // k, z - y + (m - z) // k))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
