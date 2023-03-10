import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    mask = 2 ** max(a).bit_length() - 1
    ans = []
    while mask:
        best_index = -1
        best = 0
        for i in range(n):
            if a[i] >= 0:
                if a[i] & mask > best:
                    best = a[i] & mask
                    best_index = i
        if best_index != -1:
            ans.append(a[best_index])
            mask &= ~a[best_index]
            a[best_index] = -1
        else:
            break
    for i in range(n):
        if a[i] >= 0:
            ans.append(a[i])
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
