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
    nums.sort()
    i = 0
    ans = []
    for m in range(n - 1, 0, -1):
        ans.append(nums[i])
        i += m
    ans.append(ans[-1])
    print(*ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
