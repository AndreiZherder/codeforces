from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    i = 0
    j = n - 1
    ans = 0
    sign = 1
    while i <= j:
        if a[i] * sign >= 0:
            i += 1
            continue
        if a[j] * sign >= 0:
            j -= 1
            continue
        ans += 1
        sign = -sign
    print(sum(abs(x) for x in a), ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
