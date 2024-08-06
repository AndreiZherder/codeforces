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
    a = [1 for i in range(200001)]
    a[0] = 0
    cur = 3
    x = 2
    while cur <= 531441:
        for j in range(cur, min(cur * 3, len(a))):
            a[j] = x
        cur *= 3
        x += 1
    pref = list(accumulate(a))

    t = int(input())
    while t:
        l, r = [int(num) for num in input().split()]
        num = l
        k = 0
        while num != 0:
            num //= 3
            k += 1
        ans = k
        ans += k
        ans += pref[r] - pref[l]
        t -= 1
        print(ans)



def main():
    solution()


if __name__ == '__main__':
    main()
