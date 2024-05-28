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
    x = [int(num) for num in reversed(bin(int(input()))[2:].zfill(32))]
    ans = [0 for i in range(32)]
    j = 0
    cnt = 0
    for i in range(31):
        if x[i] == 0:
            if cnt > 1:
                ans[j] = -1
                for k in range(j + 1, i):
                    ans[k] = 0
                ans[i] = 1
                cnt = 1
                j = i
            elif cnt == 1:
                ans[j] = 1
                cnt = 0
                j = i + 1
            else:
                j = i + 1
        else:
            cnt += 1
    print(len(ans))
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
