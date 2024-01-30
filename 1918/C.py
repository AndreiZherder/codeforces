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
    a, b, r = [int(num) for num in input().split()]
    step = 1
    changed = 0
    for j in range(63, -1, -1):
        if a & 1 << j != b & 1 << j:
            if step == 1:
                if b & 1 << j:
                    a, b = b, a
                step = 2
            else:
                if a & 1 << j:
                    if changed | 1 << j <= r:
                        a ^= (1 << j)
                        b ^= (1 << j)
                        changed |= 1 << j
    print(abs(a - b))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
