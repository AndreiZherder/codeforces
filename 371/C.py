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
    def bsr(left: int, right: int) -> int:
        """
        TTTTFFFF
            |
        """

        def check(mid: int) -> bool:
            have = min(nb // b if b != 0 else 10 ** 20, ns // s if s != 0 else 10 ** 20, nc // c if c != 0 else 10 ** 20)
            rb = nb - have * b
            rs = ns - have * s
            rc = nc - have * c
            need = mid - have
            if need <= 0:
                return True
            return max(0, (need * b - rb)) * pb + max(0, (need * s - rs)) * ps + max(0, (need * c - rc)) * pc <= r


        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left

    receipt = input()
    b, s, c = 0, 0, 0
    for ingridient in receipt:
        if ingridient == 'B':
            b += 1
        elif ingridient == 'S':
            s += 1
        else:
            c += 1
    nb, ns, nc = [int(num) for num in input().split()]
    pb, ps, pc = [int(num) for num in input().split()]
    r = int(input())
    print(bsr(0, 10 ** 13) - 1)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
