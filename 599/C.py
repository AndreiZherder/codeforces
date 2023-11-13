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
    sufmin = [10 ** 20 for i in range(n)]
    sufmin[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        sufmin[i] = min(sufmin[i + 1], nums[i])
    prefmax = -10 ** 20
    ans = 0
    for i in range(n - 1):
        prefmax = max(prefmax, nums[i])
        if prefmax <= sufmin[i + 1]:
            ans += 1
    print(ans + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
