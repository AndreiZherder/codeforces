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
    ans = [-1 for i in range(n)]
    j = n - 1
    i = n - 1
    prev = 0
    while i >= 0:
        while i >= 0 and s[i] == '1':
            i -= 1
        if i >= 0:
            ans[j] = j - i + prev
            prev = ans[j]
            j -= 1
            i -= 1
        else:
            print(*reversed(ans))
            return
    print(*reversed(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
