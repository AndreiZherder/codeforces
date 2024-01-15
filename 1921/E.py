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
    h, w, ya, xa, yb, xb = [int(num) for num in input().split()]
    if ya >= yb:
        print('Draw')
        return
    if (yb - ya) % 2 == 0 and xa == xb:
        print('Bob')
        return
    if (yb - ya) % 2 == 1 and abs(xa - xb) <= 1:
        print('Alice')
        return
    if (yb - ya) % 2 == 0:
        delta = (yb - ya) // 2
        if xa > xb:
            xa = min(w, xa + delta)
            if xa - (xb + delta) > 0:
                print('Draw')
                return
            else:
                print('Bob')
                return
        else:
            xa = max(1, xa - delta)
            if (xb - delta) - xa > 0:
                print('Draw')
                return
            else:
                print('Bob')
                return
    else:
        if xa > xb:
            xa -= 1
            ya += 1
        else:
            xa += 1
            ya += 1
        delta = (yb - ya) // 2
        if xb > xa:
            xb = min(w, xb + delta)
            if xb - (xa + delta) > 0:
                print('Draw')
                return
            else:
                print('Alice')
                return
        else:
            xb = max(1, xb - delta)
            if (xa - delta) - xb > 0:
                print('Draw')
                return
            else:
                print('Alice')
                return


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
