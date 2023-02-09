import sys

input = sys.stdin.readline
print_list = lambda arr: sys.stdout.write(" ".join(map(str, arr)) + "\n")


def solution():
    n = int(input())
    if n % 2 == 0:
        print('NO')
        return

    ans = []
    for i in range(1, n // 2 + 2):
        ans.append([i, n * 2 - (i - 1) * 2])
    start = n // 2 + 2
    for i in range(n // 2 + 2, n + 1):
        ans.append([i, n * 2 - (i - start) * 2 - 1])
    print('YES')
    for row in ans:
        print_list(row)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
