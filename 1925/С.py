from collections import Counter
from os import path
from string import ascii_lowercase
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
    n, k, m = [int(num) for num in input().split()]
    s = input()
    j = 0
    ans = []
    for i in range(n):
        chars = set(ascii_lowercase[:k])
        while j < m and chars:
            chars.discard(s[j])
            j += 1
        if chars:
            print('NO')
            print(''.join(ans) + chars.pop() * (n - i))
            return
        else:
            ans.append(s[j - 1])
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
