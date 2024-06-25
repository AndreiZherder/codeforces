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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    def solve(x, k) -> int:
        if x % y == 0:
            x += 1
            k -= 1
            if k == 0:
                return x
            else:
                return solve(x, k)
        c = ceil(x, y)
        if k < c * y - x:
            return x + k
        cur = c * y
        while cur % y == 0:
            cur //= y
        if k == c * y - x:
            return cur
        else:
            k -= c * y - x
            if cur == 1:
                return cur + k % (y - 1)
            return solve(cur, k)


    x, y, k = [int(num) for num in input().split()]
    print(solve(x, k))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
