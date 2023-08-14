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
    n, k = [int(num) for num in input().split()]
    if n % 2 == 0:
        if k % 2 == 0:
            if k > n:
                print('NO')
                return
            print('YES')
            print(*([1] * (k - 1) + [n - (k - 1)]))
        else:
            if k > n // 2:
                print('NO')
                return
            print('YES')
            print(*([2] * (k - 1) + [n - (k - 1) * 2]))
    elif k % 2 == 0:
        print('NO')
    else:
        if k > n:
            print('NO')
            return
        print('YES')
        print(*([1] * (k - 1) + [n - (k - 1)]))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
