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
    a = []
    for i in range(n):
        a.append(input())
    ans = []
    for i in range(n):
        j = a[i].find('.')
        if j != -1:
            ans.append((i + 1, j + 1))
        else:
            ans.clear()
            break
    if not ans:
        for j in range(n):
            for i in range(n):
                if a[i][j] == '.':
                    ans.append((i + 1, j + 1))
                    break
            else:
                ans.clear()
                break
    if not ans:
        print(-1)
    else:
        for i, j in ans:
            print(i, j)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
