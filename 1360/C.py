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


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    if n % 2 == 1:
        print('NO')
        return
    odd = 0
    even = 0
    for num in nums:
        if num % 2 == 1:
            odd += 1
        else:
            even += 1
    if odd % 2 == 0:
        print('YES')
        return
    seen = set()
    for num in nums:
        if num - 1 in seen or num + 1 in seen:
            print('YES')
            return
        else:
            seen.add(num)
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
