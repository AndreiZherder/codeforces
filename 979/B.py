from collections import Counter
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
    def play(x: str) -> int:
        s = Counter(x)
        best = 0
        for v in s.values():
            if v == m and n == 1:
                return m - 1
            best = max(best, min(v + n, m))
        return best


    n = int(input())
    s1 = input()
    s2 = input()
    s3 = input()
    m = len(s1)
    results = sorted(((play(s1), 'Kuro'), (play(s2), 'Shiro'), (play(s3), 'Katie')), reverse=True)
    if results[0][0] == results[1][0]:
        print('Draw')
    else:
        print(results[0][1])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
