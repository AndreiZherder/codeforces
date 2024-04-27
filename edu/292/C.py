from os import path
from sys import stdin, stdout


filename = '../../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, s = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    j = 0
    ans = 0
    total = 0
    for i in range(n):
        total += nums[i]
        while total > s:
            total -= nums[j]
            j += 1
        ans += i - j + 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
