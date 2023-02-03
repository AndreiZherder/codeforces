from collections import deque


def solution():
    n = int(input())
    s = deque(input())
    while len(s) > 1:
        if (s[0] == '0' and s[-1] == '1') or (s[0] == '1' and s[-1] == '0'):
            s.popleft()
            s.pop()
        else:
            print(len(s))
            return
    print(len(s))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
