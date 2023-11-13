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
    nums = sorted(int(num) for num in input().split())
    cur = []
    ans = 0
    while len(nums) >= 2:
        if nums[-1] - nums[-2] == 0:
            cur.append(nums[-1])
            cur.append(nums[-1])
            nums.pop()
            nums.pop()
        elif nums[-1] - nums[-2] == 1:
            cur.append(nums[-1] - 1)
            cur.append(nums[-1] - 1)
            nums.pop()
            nums.pop()
        else:
            nums.pop()
        if len(cur) == 4:
            ans += cur[0] * cur[-1]
            cur.clear()
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
