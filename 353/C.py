from itertools import accumulate
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
    s = input()
    pref = list(accumulate(nums, initial=0))
    best = sum(nums[i] if s[i] == '1' else 0 for i in range(n))
    total = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            best = max(best, total + pref[i])
            total += nums[i]
    print(best)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
