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


def main():
    def solution():
        n, k = [int(num) for num in input().split()]
        b = [int(num) for num in input().split()]
        k = min(k, n)
        cur = n - 1
        while k:
            if b[cur] > n:
                print('NO')
                return
            cur = (cur - b[cur]) % n
            k -= 1
        print('YES')
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
