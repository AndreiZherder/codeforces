from collections import deque
from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = deque(int(num) for num in input().split())
    cnt = 0
    ta = 0
    tb = 0
    preva = 0
    prevb = 0
    while nums:
        cnt += 1
        cura = 0
        while nums and cura <= prevb:
            cura += nums.popleft()
        ta += cura
        preva = cura
        if nums:
            cnt += 1
            curb = 0
            while nums and curb <= preva:
                curb += nums.pop()
            tb += curb
            prevb = curb
    print(cnt, ta, tb)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
