from bisect import bisect_right
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
    n, m, k = [int(num) for num in input().split()]
    s = input()
    logs = []
    crocs = []
    waters = []
    for i, c in enumerate(s):
        if c == 'L':
            logs.append(i)
        elif c == 'C':
            crocs.append(i)
        else:
            waters.append(i)
    i = -1
    while i < n:
        if i == -1 or s[i] == 'L':
            if n - i <= m:
                print('YES')
                return
            logi = bisect_right(logs, i + m) - 1
            if logi >= 0 and logs[logi] > i:
                i = logs[logi]
            else:
                wateri = bisect_right(waters, i + m) - 1
                if wateri >= 0 and waters[wateri] > i:
                    i = waters[wateri]
                else:
                    print('NO')
                    return
        elif s[i] == 'W':
            if k == 0:
                print('NO')
                return
            i += 1
            k -= 1
        else:
            print('NO')
            return
    print('YES')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
