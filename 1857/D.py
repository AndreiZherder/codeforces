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
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    c = [ai - bi for ai, bi in zip(a, b)]
    mx = max(c)
    ans = []
    for i, ci in enumerate(c):
        if ci == mx:
            ans.append(i + 1)
    print(len(ans))
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
