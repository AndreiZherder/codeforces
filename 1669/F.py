from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    i = 0
    j = n - 1
    a = 0
    b = 0
    cur = 0
    best = 0
    while i <= j:
        if a <= b:
            a += nums[i]
            i += 1
            cur += 1
        else:
            b += nums[j]
            j -= 1
            cur += 1
        if a == b:
            best = cur
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
