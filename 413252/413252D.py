def solution():
    n, a, b = (int(num) for num in input().split())
    print((a - 1 + b) % n + 1)

def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
