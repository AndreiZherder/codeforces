from functools import reduce
from itertools import accumulate
from operator import xor
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
    n = int(input())
    nums = [int(num) for num in input().split()]
    pref = list(accumulate(range(1, n + 1), xor, initial=0))
    tk = []
    for k in range(1, n + 1):
        t = n // k
        r = n % k
        if t % 2 == 1:
            tk.append(pref[r] ^ pref[k - 1])
        else:
            tk.append(pref[0] ^ pref[r])
    print(reduce(xor, tk) ^ reduce(xor, nums))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
