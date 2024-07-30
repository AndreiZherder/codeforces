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
    n = int(input())
    s1 = input()
    s2 = input()
    ans = 0
    for i in range(2, n):
        if s1[i - 2] == 'x' and s1[i - 1] == '.' and s1[i] == 'x' and s2[i - 2] == '.' and s2[i - 1] == '.' and s2[i] == '.':
            ans += 1
        if s2[i - 2] == 'x' and s2[i - 1] == '.' and s2[i] == 'x' and s1[i - 2] == '.' and s1[i - 1] == '.' and s1[i] == '.':
            ans += 1
    print(ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
