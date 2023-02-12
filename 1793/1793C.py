import sys

input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if n < 4:
        print(-1)
        return
    up = a[1] > a[0]
    i = 2
    cur = 0
    while i < n:
        if up:
            if a[i] < a[i - 1]:
                up = False
                cur, prev = i - 1, cur
                if prev - 1 >= 0:
                    if a[i] > a[prev] and a[prev - 1] < a[cur]:
                        print(prev, i + 1)
                        return
        else:
            if a[i] > a[i - 1]:
                up = True
                cur, prev = i - 1, cur
                if prev - 1 >= 0:
                    if a[i] < a[prev] and a[prev - 1] > a[cur]:
                        print(prev, i + 1)
                        return
        i += 1
    print(-1)








def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
