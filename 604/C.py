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
    s = input()
    m = 1
    prev = s[0]
    for c in s[1:]:
        if c != prev:
            m += 1
            prev = c
    add = 0
    if '00' in s or '11' in s:
        add = 1
    if '000' in s or '111' in s:
        add = 2
    else:
        i = s.find('11')
        if i != -1:
            i += 3
            i = s.find('11', i)
            if i != -1:
                add = 2
        i = s.find('00')
        if i != -1:
            i += 3
            i = s.find('00', i)
            if i != -1:
                add = 2
        i = s.find('11')
        if i != -1:
            i += 2
            i = s.find('00', i)
            if i != -1:
                add = 2
        i = s.find('00')
        if i != -1:
            i += 2
            i = s.find('11', i)
            if i != -1:
                add = 2
    print(m + add)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
