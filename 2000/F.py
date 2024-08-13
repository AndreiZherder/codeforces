from collections import defaultdict
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


def solution():
    def bsl(left: int, right: int) -> int:
        """
        FFFFTTTT
            |
        """

        def check(mid: int) -> bool:
            cur = mid
            total = 0
            for a in sorted(rectangles):
                for b in rectangles[a]:
                    for j in range(b):
                        if cur >= a:
                            total += 1
                            cur -= a
                        else:
                            if j == b - 1:
                                total += cur % a
                            return total >= k
                    total += a
                if total == k:
                    return True
            return False



        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    n, k = [int(num) for num in input().split()]
    rectangles = defaultdict(list)
    total = 0
    for i in range(n):
        a, b = [int(num) for num in input().split()]
        total += a * b
        if b < a:
            a, b = b, a
        rectangles[a].append(b)
    for a in rectangles:
        rectangles[a].sort()
    ans = bsl(0, total)
    print(ans if ans <= total else -1)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
