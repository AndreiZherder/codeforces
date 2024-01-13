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
    mn = -10 ** 20
    mx = 10 ** 20
    b = []
    for i in range(n):
        a, x = [int(num) for num in input().split()]
        if a == 1:
            mn = max(mn, x)
        elif a == 2:
            mx = min(mx, x)
        else:
            b.append(x)
    if mx < mn:
        print(0)
        return
    ans = mx - mn + 1
    for x in b:
        if mn <= x <= mx:
            ans -= 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
