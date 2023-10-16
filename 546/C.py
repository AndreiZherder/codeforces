from collections import deque
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
    n, *nums = (int(num) for num in input().split())
    a = deque(nums)
    m, *nums = (int(num) for num in input().split())
    b = deque(nums)
    seen1 = set()
    seen1.add(tuple(a))
    seen2 = set()
    seen2.add(tuple(b))
    ans = 0
    while a and b:
        x = a.popleft()
        y = b.popleft()
        if x > y:
            a.append(y)
            a.append(x)
        else:
            b.append(x)
            b.append(y)
        if tuple(a) in seen1 and tuple(b) in seen2:
            print(-1)
            return
        seen1.add(tuple(a))
        seen2.add(tuple(b))
        ans += 1
    print(ans, end=' ')
    print(1 if a else 2)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
