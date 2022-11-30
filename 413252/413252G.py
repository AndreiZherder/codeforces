def solution():
    n = int(input())
    notebooks = []
    for i in range(n):
        notebooks.append([int(num) for num in input().split()])
    notebooks.sort()
    prev = 0
    for price, quality in notebooks:
        if quality < prev:
            print('Happy Alex')
            return
        prev = quality
    print('Poor Alex')

def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
