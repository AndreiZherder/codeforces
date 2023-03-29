import sys
from typing import List

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def get_digits(num: int) -> List[int]:
        ans = []
        while num:
            ans.append(num % 10)
            num //= 10
        return ans

    a, b = [int(num) for num in input().split()]
    if a > b:
        a, b = b, a
    if b - a >= 100:
        x = b // 100 * 100 + 90
        if x > b:
            x -= 100
        elif x < a:
            x += 100
        print(x)
        return
    best = -1
    ans = []
    for i in range(a, b + 1):
        digits = get_digits(i)
        cur = max(digits) - min(digits)
        if cur > best:
            ans = digits
            best = cur
    print(*reversed(ans), sep='')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
