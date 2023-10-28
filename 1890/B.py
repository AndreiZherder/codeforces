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
    n, m = [int(num) for num in input().split()]
    s = input()
    t = input()
    ans = 'Yes'
    if '11' in s and (t[0] != '0' or t[-1] != '0' or '00' in t or '11' in t):
        ans = 'No'
    if '00' in s and (t[0] != '1' or t[-1] != '1' or '00' in t or '11' in t):
        ans = 'No'
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
