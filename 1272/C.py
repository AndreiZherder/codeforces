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
    n, k = [int(num) for num in input().split()]
    s = input()
    letters = set(input().split())
    cnt = 0
    ans = 0
    for c in s:
        if c in letters:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    ans += cnt * (cnt + 1) // 2
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
