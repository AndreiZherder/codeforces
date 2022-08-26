"""

"""


def solution(n: int, k: int, b: int, s: int):
    if k == 1:
        if b != s:
            return []
        else:
            return [s] + [0] * (n - 1)
    if s > k * (b + 1) - 1 + (n - 1) * (k - 1):
        return []
    if s < k * b:
        return []
    if s == 0 and b == 0:
        return [0] * n

    ans = []

    if k * (b + 1) - 1 >= s:
        if b != 0:
            num = k * b
            t = s // num
            ans.extend([num] * t)
            n -= t
            s -= t * num
    else:
        num = k * (b + 1) - 1
        ans.extend([num])
        n -= 1
        s -= num


    t = s // (k - 1)
    ans.extend([k - 1] * t)
    n -= t
    s -= t * (k - 1)
    if s > 0:
        ans.append(s)
        n -= 1
    ans.extend([0] * n)
    return ans


def main():
    t = int(input())
    while t:
        n, k, b, s = map(int, input().split())
        ans = solution(n, k, b, s)
        print(-1) if not ans else print(*ans)
        t -= 1


if __name__ == '__main__':
    main()
