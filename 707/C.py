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
    def calculate(n: int, m: int) -> (int, int, int):
        return m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2

    x = int(input())
    if x <= 2:
        print(-1)
        return
    if x % 2 == 0:
        print(*(y for y in calculate(1, x // 2) if y != x))
    else:
        print(*(y for y in calculate((x + 1) // 2 - 1, (x + 1) // 2) if y != x))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
