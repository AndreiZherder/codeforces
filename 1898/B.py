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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    prev = nums[n - 1]
    ans = 0
    for i in range(n - 2, -1, -1):
        if prev >= nums[i]:
            prev = nums[i]
            continue
        if prev * 2 >= nums[i]:
            ans += 1
            prev = nums[i] // 2
        else:
            k = ceil(nums[i], prev)
            ans += k - 1
            prev = nums[i] // k
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
