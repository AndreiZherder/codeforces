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
    n, k = [int(num) for num in input().split()]
    a = []
    for i in range(k):
        m, *row = [int(num) for num in input().split()]
        a.append(row)
    parts = 0
    ans = 0
    for row in a:
        if len(row) == 1:
            parts += 1
        elif row[0] != 1:
            parts += len(row)
            ans += len(row) - 1
        else:
            for i in range(1, len(row)):
                if row[i] != row[i - 1] + 1:
                    parts += 1 + len(row) - i
                    ans += len(row) - i
                    break
            else:
                parts += 1
    print(ans + parts - 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
