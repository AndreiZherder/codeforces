from itertools import product, combinations, permutations
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
    def check(target: str, guess: str, gb: int, gc: int) -> bool:
        b = 0
        c = 0
        for x in guess:
            if x in target:
                c += 1
        for x1, x2 in zip(target, guess):
            if x1 == x2:
                b += 1
                c -= 1
        return b == gb and c == gc

    n = int(input())
    attempts = []
    for i in range(n):
        guess, gb, gc = input().split()
        attempts.append([guess, int(gb), int(gc)])
    cnt = 0
    for target in permutations(range(10), 4):
        if all(check(''.join(map(str, target)), guess, gb, gc) for guess, gb, gc in attempts):
            cnt += 1
            ans = ''.join(map(str, target))
        if cnt == 2:
            print('Need more data')
            return
    if cnt == 1:
        print(ans)
    else:
        print('Incorrect data')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
