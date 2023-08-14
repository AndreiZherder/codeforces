from itertools import islice, cycle
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
    n0, n2, n1 = [int(num) for num in input().split()]
    ans0 = ''
    ans1 = ''
    ans2 = ''
    if n1 != 0:
        ans1 = '1' * (n1 + 1)
    if n0 != 0:
        ans0 = '0' * (n0 + 1)
    if n2 != 0:
        if n1 == 0 and n0 == 0:
            ans2 = ''.join(islice(cycle('10'), n2 + 1))
        elif n0 == 0:
            ans2 = ''.join(islice(cycle('01'), (n2 - 1) + 1))
        elif n1 == 0:
            ans2 = ''.join(islice(cycle('10'), (n2 - 1) + 1))
        else:
            ans2 = ''.join(islice(cycle('10'), (n2 - 2) + 1))
    print(ans1 + ans0 + ans2)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
