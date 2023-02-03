

def sum_of_digits(num: int) -> int:
    ans = 0
    while num:
        ans += num % 10
        num //= 10
    return ans


def solution():
    n, q = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    next = [i + 1 for i in range(n + 2)]
    prev = [i - 1 for i in range(n + 2)]
    while q:
        cmd = input().split()
        if cmd[0] == '1':
            l, r = int(cmd[1]) - 1, int(cmd[2]) - 1
            i = l
            while i < n and i <= r:
                if a[i] > 9:
                    a[i] = sum_of_digits(a[i])
                    if a[i] < 10:
                        next[prev[i + 1]] = next[i + 1]
                        prev[next[i + 1]] = prev[i + 1]
                        i = next[prev[i + 1]] - 1
                    else:
                        i = next[i + 1] - 1
                else:
                    i = next[prev[i + 1]] - 1

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
