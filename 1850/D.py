from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    nums = sorted([int(num) for num in input().split()])
    best = 1
    cur = 1
    for i in range(1, n):
        if nums[i] - nums[i - 1] <= k:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
    print(n - best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
