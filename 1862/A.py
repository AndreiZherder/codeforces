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
    def check(j: int, c: str) -> bool:
        for k in range(n):
            if a[k][j] == c:
                return True
        return False

    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    s = 'vika'
    i = 0
    j = 0
    while i < len(s):
        if check(j, s[i]):
            i += 1
            j += 1
        else:
            j += 1
        if j == m and i < len(s):
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
