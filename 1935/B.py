from os import path
from sys import stdin, stdout
from typing import List

filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)

def get_mex_pref(nums: List[int], n: int) -> List[int]:
    ans = []
    s = [False for i in range(n + 1)]
    i = 0
    for num in nums:
        s[num] = True
        while s[i]:
            i += 1
        ans.append(i)
    return ans


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    mex_pref = get_mex_pref(nums, n)
    mex_suf = get_mex_pref(nums[::-1], n)[::-1]
    ans = -1
    for i in range(n - 1):
        if mex_pref[i] == mex_suf[i + 1]:
            ans = i
    if ans == -1:
        print(ans)
    else:
        print(2)
        print(1, ans + 1)
        print(ans + 2, n)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
