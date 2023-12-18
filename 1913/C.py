from collections import Counter
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
    m = int(input())
    counter = Counter()
    for i in range(m):
        t, v = [int(num) for num in input().split()]
        if t == 1:
            counter[1 << v] += 1
        else:
            for j in range(29, -1, -1):
                x = v // (1 << j)
                v -= min(x, counter[1 << j]) * (1 << j)
                if v == 0:
                    print('YES')
                    break
            else:
                print('NO')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
