from itertools import accumulate
from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    s = input()
    i = 0
    j = n - 1
    pref = list(accumulate(a, initial=0))
    ans = 0
    while i < j:
        i = s.find('L', i)
        j = s.rfind('R', 0, j + 1)
        if i != -1 and j != -1 and i < j:
            ans += pref[j + 1] - pref[i]
            i += 1
            j -= 1
        else:
            break
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
