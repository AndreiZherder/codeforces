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
    def get_sign(num: int) -> int:
        return 1 if num > 0 else 0
    n = int(input())
    nums = [int(num) for num in input().split()]
    sign = get_sign(nums[0])
    mx = nums[0]
    total = 0
    for num in nums[1:]:
        if get_sign(num) == sign:
            mx = max(mx, num)
        else:
            sign ^= 1
            total += mx
            mx = num
    print(total + mx)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
