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
    k = 2
    r = 10 ** 18
    while k <= r:
        seen = set()
        for num in nums:
            seen.add(num % k)
            if len(seen) == 3:
                break
        if len(seen) == 2:
            print(k)
            return
        else:
            k *= 2


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
