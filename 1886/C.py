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


def sn(a1: int, an: int, n: int) -> int:
    return (a1 + an) * n // 2


def solution():
    def bsl(left: int, right: int) -> int:
        """
        FFFFTTTT
            |
        """

        def check(mid: int) -> bool:
            return pos <= sn(len(s), len(s) - mid, mid + 1)

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    s = input()
    pos = int(input())
    x = bsl(0, len(s))
    y = sn(len(s), len(s) - x, x + 1) - pos
    stack = []
    i = 0
    while x:
        if i < len(s):
            if stack:
                if stack[-1] >= s[i]:
                    stack.pop()
                    x -= 1
                else:
                    stack.append(s[i])
                    i += 1
            else:
                stack.append(s[i])
                i += 1
        else:
            break
    while x:
        stack.pop()
        x -= 1
    word = ''.join(stack) + s[i:]
    print(word[-1 - y], end='')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
