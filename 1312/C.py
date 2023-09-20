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
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    seen = set()
    for x in a:
        while x != 0:
            i = 0
            cur = x
            while cur % k == 0:
                cur //= k
                i += 1

            if i in seen:
                print('NO')
                return
            else:
                seen.add(i)

            x -= pow(k, i)
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
