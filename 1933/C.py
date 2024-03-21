from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    a, b, l = [int(num) for num in input().split()]
    ans = set()
    x = 0
    cur_a = 1
    while l % cur_a == 0:
        cur_l = l // cur_a
        cur_b = 1
        while cur_l % cur_b == 0:
            ans.add(cur_l // cur_b)
            cur_b *= b
        cur_a *= a

    a, b = b, a

    cur_a = 1
    while l % cur_a == 0:
        cur_l = l // cur_a
        cur_b = 1
        while cur_l % cur_b == 0:
            ans.add(cur_l // cur_b)
            cur_b *= b
        cur_a *= a

    print(len(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
