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
    if n == 1 or all(nums[i] == nums[0] for i in range(n)):
        print(0)
        return
    if nums[0] == nums[-1]:
        j = 0
        while nums[j] == nums[0]:
            j += 1
        i = n - 1
        while nums[i] == nums[n - 1]:
            i -= 1
        print(i - j + 1)
    else:
        j = 0
        while nums[j] == nums[0]:
            j += 1
        i = n - 1
        while nums[i] == nums[n - 1]:
            i -= 1
        x = max(j, n - i - 1)
        print(n - x)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
