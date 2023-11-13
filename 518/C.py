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
    n, m, k = [int(num) for num in input().split()]
    a = [int(num) - 1 for num in input().split()]
    b = [int(num) - 1 for num in input().split()]
    place = {ai: i for i, ai in enumerate(a)}
    ans = 0
    for bi in b:
        ans += 1 + place[bi] // k
        if place[bi] != 0:
            a[place[bi] - 1], a[place[bi]] = a[place[bi]], a[place[bi] - 1]
            place[a[place[bi]]] = place[bi]
            place[bi] -= 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
