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
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    i = 0
    j = 0
    ans = []
    while j < m:
        if i == n:
            print('NO')
            return
        if s[i] == t[j]:
            ans.append(t[j])
            i += 1
            j += 1
        elif s[i] == '?':
            ans.append(t[j])
            i += 1
            j += 1
        else:
            ans.append(s[i])
            i += 1
    while i < n:
        if s[i] == '?':
            ans.append('a')
        else:
            ans.append(s[i])
        i += 1
    print('YES')
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
