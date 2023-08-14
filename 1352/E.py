from itertools import accumulate
from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    if n < 3:
        print(0)
        return
    pref = list(accumulate(nums, initial=0))
    s = set()
    for i in range(n + 1):
        for j in range(i + 2, n + 1):
            total = pref[j] - pref[i]
            if 1 <= total <= n:
                s.add(total)
    ans = 0
    for num in nums:
        if num in s:
            ans += 1
    print(ans)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
