from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    time, n = input().split()
    time = int(time[:2]) * 60 + int(time[3:])
    n = int(n)
    seen = set()
    ans = 0
    while time not in seen:
        seen.add(time)
        h = str(time // 60).zfill(2)
        m = str(time % 60).zfill(2)
        if h == m[::-1]:
            ans += 1
        time = (time + n) % 1440
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
