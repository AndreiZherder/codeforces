from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    m = int(input())
    a = [int(num) for num in input().split()]
    step = 2
    ans = 0
    while step <= m:
        for i in range(0, m, step):
            if a[i + step // 2] < a[i]:
                a[i:i + step // 2], a[i + step // 2:i + step] = a[i + step // 2:i + step], a[i:i + step // 2]
                ans += 1
            for j in range(i + 1, i + step):
                if a[j] - a[j - 1] != 1:
                    print(-1)
                    return
        step *= 2
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
