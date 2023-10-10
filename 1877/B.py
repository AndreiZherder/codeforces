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
    n, p = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    a.append(n - 1)
    b.append(p)
    s = sorted(([ai, bi] for ai, bi in zip(a, b)), key=lambda x: (x[1], -x[0]))
    ans = p
    n -= 1
    i = 0
    while n:
        x = min(n, s[i][0])
        ans += x * s[i][1]
        i += 1
        n -= x
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
