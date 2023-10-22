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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    if k == 4:
        cnt = 0
        for ai in a:
            if ai % 2 == 0:
                cnt += 1
        if cnt >= 2:
            print(0)
            return
        elif cnt == 1:
            print(min(1, min(ceil(ai, k) * k - ai for ai in a)))
            return
        else:
            print(min(2, min(ceil(ai, k) * k - ai for ai in a)))
            return
    else:
        print(min(ceil(ai, k) * k - ai for ai in a))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
