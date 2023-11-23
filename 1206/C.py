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
    n = int(input())
    if n % 2 == 0:
        print('NO')
    else:
        print('YES')
        ans = [0 for i in range(2 * n)]
        cur = 0
        for i in range(0, 2 * n, 2):
            ans[cur] = i + 1
            cur = (cur + n) % (2 * n)
            ans[cur] = i + 2
            cur = (cur - 1) % (2 * n)
        print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
