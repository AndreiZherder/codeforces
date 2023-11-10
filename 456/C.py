from collections import Counter
from os import path
from random import getrandbits
from sys import stdin, stdout
from types import GeneratorType

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


RANDOM = getrandbits(32)


class Int(int):
    def __hash__(self):
        return super().__hash__() ^ RANDOM


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc

def solution():
    @bootstrap
    def dp(i: int) -> int:
        if i in cache:
            yield cache[i]
        if i >= n:
            ans = 0
        elif i == n - 1:
            ans = nums[n - 1] * c[nums[n - 1]]
        else:
            ans1 = yield dp(i + 1)
            ans2 = nums[i] * c[nums[i]]
            if nums[i + 1] - nums[i] == 1:
                ans2 += yield dp(i + 2)
            else:
                ans2 += yield dp(i + 1)
            ans = max(ans1, ans2)
        cache[i] = ans
        yield ans


    n = int(input())
    nums = [Int(num) for num in input().split()]
    c = Counter(nums)
    nums = sorted(c)
    n = len(nums)
    cache = dict()
    print(dp(0))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
