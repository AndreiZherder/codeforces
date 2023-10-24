from collections import Counter, defaultdict
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
    n, q = [int(num) for num in input().split()]
    apps = [[0, False] for i in range(300000)]
    messages = [[] for i in range(n)]
    total = 0
    cur = 0
    ans = []
    pos = 0
    while q:
        type, x = (int(num) for num in input().split())
        if type == 1:
            x -= 1
            apps[pos] = [x, False]
            messages[x].append(pos)
            pos += 1
            total += 1
        elif type == 2:
            x -= 1
            a = messages[x]
            while a:
                i = a.pop()
                if not apps[i][1]:
                    apps[i][1] = True
                    total -= 1
        else:
            for i in range(cur, x):
                if not apps[i][1]:
                    apps[i][1] = True
                    total -= 1
            cur = max(cur, x)
        ans.append(f'{total}')
        q -= 1
    print('\n'.join(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
