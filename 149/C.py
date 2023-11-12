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
    a = sorted((num, i) for i, num in enumerate(nums))
    print((n + 1) // 2)
    print(*(a[index][1] + 1 for index in range(0, n, 2)))
    print(n // 2)
    print(*(a[index][1] + 1 for index in range(1, n, 2)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
