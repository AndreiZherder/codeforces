from os import path
from sys import stdin, stdout


filename = '../../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, c = [int(num) for num in input().split()]
    s = input()
    best = 0
    j = 0
    score = 0
    cnta = 0
    cntb = 0
    for i in range(n):
        if s[i] == 'a':
            cnta += 1
        elif s[i] == 'b':
            cntb += 1
            score += cnta
        while score > c:
            if s[j] == 'a':
                score -= cntb
                cnta -= 1
            elif s[j] == 'b':
                cntb -= 1
            j += 1
        best = max(best, i - j + 1)
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
