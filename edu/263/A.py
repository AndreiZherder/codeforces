from os import path
from sys import stdin, stdout


if path.exists("../../templates/input.txt"):
    stdin = open("../../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    xs = []
    vs = []
    for i in range(n):
        x, v = [int(num) for num in input().split()]
        xs.append(x)
        vs.append(v)

    def check(mid: float) -> bool:
        return min(x + mid * v for x, v in zip(xs, vs)) >= max(x - mid * v for x, v in zip(xs, vs))

    left = 0
    right = 2 * 10 ** 9 / min(vs)
    for i in range(100):
        mid = left + (right - left) / 2
        if check(mid):
            right = mid
        else:
            left = mid
    print(left)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
