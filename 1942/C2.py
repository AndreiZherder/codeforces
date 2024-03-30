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
    n, x, y = [int(num) for num in input().split()]
    nums = sorted([int(num) for num in input().split()])
    ans = x - 2
    even = []
    odd = []

    for num1, num2 in zip(nums, nums[1:]):
        if (num2 - num1) % 2 == 0:
            even.append(num2 - num1)
        else:
            odd.append(num2 - num1)
    if ((nums[0] - nums[-1]) % n) % 2 == 0:
        even.append((nums[0] - nums[-1]) % n)
    else:
        odd.append((nums[0] - nums[-1]) % n)

    even.sort()
    odd.sort()
    for d in even:
        if d > 2:
            if y >= d // 2 - 1:
                ans += d // 2 + d // 2 - 1
                y -= d // 2 - 1
            else:
                ans += y + y
                y = 0
        else:
            ans += 1

    if y > 0:
        for d in odd:
            if d > 2:
                if y >= d // 2:
                    ans += d // 2 + d // 2
                    y -= d // 2
                else:
                    ans += y + y
                    break

    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
