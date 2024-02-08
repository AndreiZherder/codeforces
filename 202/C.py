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
    ans = [0 for i in range(101)]
    for i in range(3, 14):
        ans[i] = 5
    ans[5] = 3
    for i in range(14, 26):
        ans[i] = 7
    for i in range(26, 42):
        ans[i] = 9
    for i in range(42, 62):
        ans[i] = 11
    for i in range(62, 86):
        ans[i] = 13
    for i in range(86, 101):
        ans[i] = 15
    ans[1] = 1
    ans[2] = 3
    ans[4] = 3
    print(ans[int(input())])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
