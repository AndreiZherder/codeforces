import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    for i in range(n):
        _, cmds = input().split()
        for cmd in cmds:
            if cmd == 'U':
                a[i] -= 1
            else:
                a[i] += 1
    print(*[num % 10 for num in a])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
