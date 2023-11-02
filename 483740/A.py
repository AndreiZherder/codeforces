def solution():
    def get_sum(s: str) -> int:
        return sum(int(c) for c in s)
    s = input()
    print('YES' if get_sum(s[:3]) == get_sum(s[3:]) else 'NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
