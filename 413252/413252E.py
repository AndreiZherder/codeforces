def solution():
    s = input() + 'A'
    j = -1
    best = 0
    for i, c in enumerate(s):
        if c in 'AEIOUY':
            best = max(best, i - j)
            j = i
    print(best)

def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
