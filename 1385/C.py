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
    i = n - 1
    prev = -10 ** 20
    state = 1
    while i >= 0:
        if state == 1:
            if nums[i] < prev:
              state = 2
        if state == 2:
            if nums[i] > prev:
                print(i + 1)
                return
        prev = nums[i]
        i -= 1
    print(0)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
