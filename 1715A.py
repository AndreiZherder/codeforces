"""

"""


def solution(n: int, m: int):
    if n == 1 and m == 1:
        return 0
    return m - 1 + n - 1 + min(n - 1, m - 1) + 1


def main():
    t = int(input())
    while t:
        n, m = map(int, input().split())
        print(solution(n, m))
        t -= 1


if __name__ == '__main__':
    main()
