import sys


def solution():
    line = ''
    while not line:
        line = sys.stdin.readline().strip()
    xs = []
    ys = []
    x, y = (int(num) for num in line.split())
    xs.append(x)
    ys.append(y)
    for i in range(2):
        x, y = (int(num) for num in input().split())
        xs.append(x)
        ys.append(y)
    xs.sort()
    ys.sort()
    if xs[0] < xs[1] < xs[2] or ys[0] < ys[1] < ys[2]:
        print('YES')
    else:
        print("NO")


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
