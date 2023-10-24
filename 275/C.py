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
    n, k = [int(num) for num in input().split()]
    nums = sorted([int(num) for num in input().split()])
    s = set(nums)
    seen = set()
    ans = 0
    for num in nums:
        if num not in seen:
            s.remove(num)
            seen.add(num)
            cnt = 1
            while num * k in s:
                num *= k
                seen.add(num)
                cnt += 1
            ans += ceil(cnt, 2)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
