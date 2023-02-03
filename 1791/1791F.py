

def sum_of_digits(num: int) -> int:
    ans = 0
    while num:
        ans += num % 10
        num //= 10
    return ans


def solution():
    n, q = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    next = [i + 1 for i in range(n)]
    prev = [i - 1 for i in range(n)]
    while q:
        cmd = input().split()
        if cmd[0] == '1':
            l, r = int(cmd[1]) - 1, int(cmd[2]) - 1
            i = l
            while i < n and i <= r:
                if a[i] > 10:
                    a[i] = sum_of_digits(a[i])
                    if a[i] < 10:
                        if prev[i] >= 0:
                            next[prev[i]] = next[i]
                        if next[i] < n:
                            prev[next[i]] = prev[i]
                i = next[i]

        else:
            print(a[int(cmd[1]) - 1])
        q -= 1


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
