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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    def solve(a: List[int], b: List[int], c: List[int]) -> (bool, List[int]):
        def solve_one(nums: List[int], i: int) -> int:
            total = 0
            j = i
            while j < n and total < target:
                total += nums[j]
                j += 1
            if j == n and total < target:
                return n
            else:
                return j - 1

        la, ra, lb, rb, lc, rc = 0, 0, 0, 0, 0, 0
        r = solve_one(a, 0)
        if r != n:
            la = 0
            ra = r
        else:
            return False, [-1, -1, -1, -1, -1, -1]
        lb = r + 1
        r = solve_one(b, r + 1)
        if r != n:
            rb = r
        else:
            return False, [-1, -1, -1, -1, -1, -1]
        lc = r + 1
        r = solve_one(c, r + 1)
        if r != n:
            rc = n - 1
        else:
            return False, [-1, -1, -1, -1, -1, -1]
        return True, [la + 1, ra + 1, lb + 1, rb + 1, lc + 1, rc + 1]

    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    c = [int(num) for num in input().split()]
    total = sum(a)
    target = ceil(total, 3)
    ok, (la, ra, lb, rb, lc, rc) = solve(a, b, c)
    if ok:
        print(la, ra, lb, rb, lc, rc)
        return
    ok, (la, ra, lc, rc, lb, rb) = solve(a, c, b)
    if ok:
        print(la, ra, lb, rb, lc, rc)
        return
    ok, (lb, rb, la, ra, lc, rc) = solve(b, a, c)
    if ok:
        print(la, ra, lb, rb, lc, rc)
        return
    ok, (lb, rb, lc, rc, la, ra) = solve(b, c, a)
    if ok:
        print(la, ra, lb, rb, lc, rc)
        return
    ok, (lc, rc, la, ra, lb, rb) = solve(c, a, b)
    if ok:
        print(la, ra, lb, rb, lc, rc)
        return
    ok, (lc, rc, lb, rb, la, ra) = solve(c, b, a)
    if ok:
        print(la, ra, lb, rb, lc, rc)
        return
    print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
