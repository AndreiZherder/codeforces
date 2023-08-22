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
    i = -1
    j = n
    s1 = 0
    s2 = 0
    best = 0
    while i < j:
        if s1 == s2:
            best = max(best, s1)
            i += 1
            s1 += nums[i]
        elif s1 > s2:
            j -= 1
            s2 += nums[j]
        else:
            i += 1
            s1 += nums[i]
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
