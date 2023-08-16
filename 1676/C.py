from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    words = []
    for i in range(n):
        words.append(input())
    best = 10 ** 20
    for i in range(n):
        for j in range(i + 1, n):
            cur = 0
            for a, b in zip(words[i], words[j]):
                cur += abs(ord(a) - ord(b))
            best = min(best, cur)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
