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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n = int(input())
    s = input()
    pref = [0]
    for i in range(n):
        pref.append(pref[-1] + (1 if s[i] == '0' else 0))
    suf = [0]
    for i in range(n - 1, -1, -1):
        suf.append(suf[-1] + (1 if s[i] == '1' else 0))
    suf.reverse()
    best = n - 1

    j = n - 1
    i = -1
    while i <= j:
        if ceil(j + 1, 2) <= pref[j + 1] and ceil(n - 1 - j, 2) <= suf[j + 1]:
            best = j
        if ceil(i + 1, 2) <= pref[i + 1] and ceil(n - 1 - i, 2) <= suf[i + 1]:
            best = i
        j -= 1
        i += 1
    print(best + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
