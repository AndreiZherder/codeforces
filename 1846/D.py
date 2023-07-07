from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, d, h = [int(num) for num in input().split()]
    y = sorted((int(num) for num in input().split()))
    ans = 0
    for i in range(n - 1):
        if y[i + 1] < y[i] + h:
            d2 = -2 * ((y[i + 1] - y[i] - h) * d / 2 / h)
            ans += (d + d2) * (y[i + 1] - y[i]) / 2
        else:
            ans += d * h / 2
    ans += d * h / 2
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
