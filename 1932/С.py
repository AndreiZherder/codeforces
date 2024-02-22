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
    n, m = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    s = input()
    path = []
    i = 0
    j = n - 1
    for c in s:
        if c == 'L':
            path.append(nums[i])
            i += 1
        else:
            path.append(nums[j])
            j -= 1
    ans = []
    cur = 1
    for num in reversed(path):
        cur = (cur * num) % m
        ans.append(cur)
    print(*reversed(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
