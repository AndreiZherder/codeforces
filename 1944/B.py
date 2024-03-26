from collections import Counter, deque
from os import path
from random import getrandbits
from sys import stdin, stdout


filename = '../templates/input.txt'
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


def solution():
    n, k = [int(num) for num in input().split()]
    n *= 2
    k *= 4
    nums = [Int(num) for num in input().split()]
    c1 = Counter(nums[:n // 2])
    c2 = Counter(nums[n // 2:])
    a = [num for num in c2 if c2[num] == 2]
    ans = deque()
    for num in sorted(c1, key=c1.get, reverse=True):
        if c1[num] == 2:
            ans.appendleft(num)
            ans.appendleft(num)
            x = a.pop()
            ans.append(x)
            ans.append(x)
            del c2[x]
        elif num in c2:
            ans.appendleft(num)
            ans.append(num)
        if len(ans) == k:
            break
    print(*list(ans)[:k // 2])
    print(*list(ans)[k // 2:])




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
