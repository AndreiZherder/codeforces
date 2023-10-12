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
    x = input()
    s = input()
    ans = 0
    if s in x:
        print(0)
        return
    if s in x * 2:
        print(1)
        return
    while len(x) <= 4 * m:
        if s in x:
            print(ans)
            return
        x *= 2
        ans += 1
    print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
