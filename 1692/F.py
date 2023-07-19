from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    c = sorted(Counter((num % 10) for num in nums).items())
    m = len(c)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if (c[i][0] + c[j][0] + c[k][0]) % 10 == 3:
                    if i != j and i != k and j != k:
                        print('YES')
                        return
                    elif i == j == k:
                        if c[i][1] >= 3:
                            print('YES')
                            return
                    elif i == j or i == k:
                        if c[i][1] >= 2:
                            print('YES')
                            return
                    elif j == k:
                        if c[j][1] >= 2:
                            print('YES')
                            return
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
