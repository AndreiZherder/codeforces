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
    def check(x: int, y: int, z: int) -> int:
        if (y - z) % 2 != 0:
            return 0
        return 1
    x, y, z = [int(num) for num in input().split()]
    if y >= z:
        ans1 = check(x, y, z)
    else:
        ans1 = check(x, z, y)
    if x >= z:
        ans2 = check(y, x, z)
    else:
        ans2 = check(y, z, x)
    if y >= x:
        ans3 = check(z, y, x)
    else:
        ans3 = check(z, x, y)
    print(ans1, ans2, ans3)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
