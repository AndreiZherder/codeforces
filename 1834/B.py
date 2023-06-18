from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    s1, s2 = input().split()
    n = len(s1)
    m = len(s2)
    if n < m:
        s1 = s1.zfill(m)
    if n > m:
        s2 = s2.zfill(n)
    ans = 0
    n = max(n, m)
    for i in range(n):
        if s1[i] != s2[i]:
            print(abs(int(s1[i]) - int(s2[i])) + 9 * (n - i - 1))
            return
    print(0)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
