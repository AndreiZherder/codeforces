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
    m1 = nums[0]
    m2 = 10 ** 20
    for i in range(1, n):
        if nums[i] < m1:
            m1, m2 = nums[i], m1
        elif nums[i] < m2 and nums[i] != m1:
            m2 = nums[i]
    if m2 == 10 ** 20:
        print('NO')
    else:
        print(m2)




def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
