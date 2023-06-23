from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def go(j: int):
        cnt = 0
        pos = n
        for i in range(n - 1, -1, -1):
            if a[i][j] == 'o':
                for k in range(cnt):
                    a[pos - k - 1][j] = '*'
                for k in range(pos - i - 1 - cnt):
                    a[pos - cnt - k - 1][j] = '.'
                pos = i
                cnt = 0
            elif a[i][j] == '*':
                cnt += 1
        i = -1
        for k in range(cnt):
            a[pos - k - 1][j] = '*'
        for k in range(pos - i - 1 - cnt):
            a[pos - cnt - k - 1][j] = '.'


    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(list(input()))
    for j in range(m):
        go(j)
    for i in range(n):
        print(''.join(a[i]))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
