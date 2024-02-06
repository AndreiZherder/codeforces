from os import path
from string import ascii_lowercase
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
    nums = [int(num) for num in input().split()]
    p = [set() for i in range(n + 1)]
    p[0] = set(ascii_lowercase)
    ans = []
    for num in nums:
        c = p[num].pop()
        ans.append(c)
        p[num + 1].add(c)
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
