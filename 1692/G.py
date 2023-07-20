from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    ans = 0
    cur = 1
    for i in range(1, n):
        if 2 * nums[i] > nums[i - 1]:
            cur += 1
        else:
            ans += max(0, cur - k)
            cur = 1
    ans += max(0, cur - k)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
