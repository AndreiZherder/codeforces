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
    avg = sum(nums) // n
    if nums[-1] > avg:
        print('NO')
        return
    j = n - 1
    for i in range(n - 2, -1, -1):
        if nums[i] > avg:
            x = nums[i] - avg
            while x:
                if nums[j] < avg:
                    y = min(x, avg - nums[j])
                    x -= y
                    nums[i] -= y
                    nums[j] += y
                if nums[j] == avg:
                    j -= 1
                if x and j == i:
                    print('NO')
                    return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
