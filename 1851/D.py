from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = [0] + [int(num) for num in input().split()]
    diff = [nums[i] - nums[i - 1] for i in range(1, n)]
    perm = set(range(1, n + 1))
    total = 0
    rest = []
    for num in diff:
        if num in perm:
            perm.remove(num)
            total += num
        else:
            rest.append(num)
    if not rest:
        print('YES')
        return
    if len(rest) > 1:
        print('NO')
        return
    if rest[0] == (1 + n) * n // 2 - total:
        print('YES')
    else:
        print('NO')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
