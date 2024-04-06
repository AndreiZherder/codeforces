from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    k -= 1
    nums = [int(num) for num in input().split()]
    ans1 = 0
    ans2 = 0
    for i in range(k):
        if nums[i] > nums[k]:
            nums[i], nums[k] = nums[k], nums[i]
            if i != 0:
                ans1 = 1
            else:
                ans1 = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    ans1 += 1
                else:
                    break
            nums[k], nums[i] = nums[i], nums[k]
            break
    nums[0], nums[k] = nums[k], nums[0]
    for j in range(1, n):
        if nums[j] < nums[0]:
            ans2 += 1
        else:
            break
    print(max(ans1, ans2))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
