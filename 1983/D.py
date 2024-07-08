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


# https://codeforces.com/blog/entry/92130?#comment-808339
def merge_sort(A):
    if len(A) <= 1:
        return A, 0
    nhalf = len(A) >> 1
    A1, invcount1 = merge_sort(A[:nhalf])
    A2, invcount2 = merge_sort(A[nhalf:])

    B = []
    invcount = invcount1 + invcount2
    A1.reverse()
    A2.reverse()
    while A1 or A2:
        if not A2 or (A1 and A1[-1] <= A2[-1]):
            B.append(A1.pop())
        else:
            invcount += len(A1)
            B.append(A2.pop())
    return B, invcount


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    a, invcount_a = merge_sort(a)
    b, invcount_b = merge_sort(b)
    print('YES' if a == b and invcount_a % 2 == invcount_b % 2 else 'NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
