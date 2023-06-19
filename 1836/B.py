from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k, g = [int(num) for num in input().split()]
    s = k * g
    x = (g - 1) // 2
    if x * n >= s:
        print(s)
    else:
        ans = x * (n - 1)
        rem = s - x * n
        y = (x + rem) % g
        if y <= x:
            ans += y
        else:
            ans -= (g - y)
        print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
