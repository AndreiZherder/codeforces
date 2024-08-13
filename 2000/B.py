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
    n = int(input())
    nums = [Int(num) for num in input().split()]
    seen = {nums[0]}
    for num in nums[1:]:
        if Int(num + 1) not in seen and Int(num - 1) not in seen:
            print('NO')
            return
        seen.add(num)
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
