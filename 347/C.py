from math import gcd
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
    g = nums[0]
    mx = nums[0]
    for i in range(1, n):
        g = gcd(g, nums[i])
        mx = max(mx, nums[i])
    if (mx // g - n) % 2 == 1:
        print('Alice')
    else:
        print('Bob')




def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
