import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    answers = []
    j = 0
    for i in range(1, n):
        if b[i] < b[i - 1]:
            answers.append((i - j, j, i - 1))
            j = i
    answers.append((n - j, j, n - 1))
    answers.sort(reverse=True)
    for length, j, i in answers:
        if b[j:i + 1] != a[j:i + 1]:
            print(j + 1, i + 1)
            return


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
