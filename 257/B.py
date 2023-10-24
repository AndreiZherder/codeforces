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
    def play(n: int, m: int) -> (int, int):
        n -= 1
        last = 0
        player = 1
        score1 = 0
        score2 = 0
        while n and m:
            if player == 1:
                if last == 0:
                    m -= 1
                    score2 += 1
                else:
                    n -= 1
                    score2 += 1
            else:
                if last == 0:
                    n -= 1
                    score1 += 1
                else:
                    m -= 1
                    score1 += 1
        if n:
            if last == 0:
                score1 += n
            else:
                score2 += 1
                score1 += n - 1
        else:
            if last == 1:
                score1 += m
            else:
                score2 += 1
                score1 += m - 1
        return score1, score2

    n, m = [int(num) for num in input().split()]
    x1, y1 = play(n, m)
    x2, y2 = play(m, n)
    if x1 - y1 >= x2 - y2:
        print(x1, y1)
    else:
        print(x2, y2)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
