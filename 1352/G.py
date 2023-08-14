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
    n = int(input())
    if n < 4:
        print(-1)
        return
    nums = list(range(1, n + 1))
    print(*(nums[::2][::-1] + [4, 2] + nums[5::2]))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
