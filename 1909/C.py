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
    ls = [int(num) for num in input().split()]
    rs = [int(num) for num in input().split()]
    cs = sorted([int(num) for num in input().split()], reverse=True)
    xs = []
    for l in ls:
        xs.append((l, 'L'))
    for r in rs:
        xs.append((r, 'R'))
    xs.sort()
    lengths = []
    stack = []
    for x, c in xs:
        if c == 'L':
            stack.append(x)
        else:
            lengths.append(x - stack.pop())
    lengths.sort()
    ans = 0
    for c, length in zip(cs, lengths):
        ans += c * length
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
