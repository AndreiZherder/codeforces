import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    s = set(words)
    ans = []
    for word in words:
        for i in range(len(word)):
            if word[:i + 1] in s and word[i + 1:] in s:
                ans.append('1')
                break
        else:
            ans.append('0')
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
