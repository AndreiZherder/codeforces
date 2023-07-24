from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    mx = -10 ** 20
    maxi = 0
    for i in range(n):
        x, y = (int(num) for num in input().split())
        if x <= 10:
            if y > mx:
                mx = y
                maxi = i
    print(maxi + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
