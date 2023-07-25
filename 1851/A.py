from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m, k, H = [int(num) for num in input().split()]
    h = [int(num) for num in input().split()]
    s = {i * k for i in range(1, m)}
    ans = 0
    for num in h:
        if abs(num - H) in s:
            ans += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
