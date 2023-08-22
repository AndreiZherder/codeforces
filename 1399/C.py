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
    def count(target: int) -> int:
        ans = 0
        i = 0
        j = n - 1
        while i < j:
            if nums[i] + nums[j] == target:
                ans += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return ans

    n = int(input())
    nums = [int(num) for num in input().split()]
    nums.sort()
    targets = set()
    for i in range(n):
        for j in range(i + 1, n):
            targets.add(nums[i] + nums[j])
    best = 0
    for target in targets:
        best = max(best, count(target))
    print(best)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
