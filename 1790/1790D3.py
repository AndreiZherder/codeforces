from collections import Counter


def get():
    n = 2 * 10 ** 5
    mask = (1 << 17) - 1
    fill = int((1 << 15) * 1.3 + 1)

    arr = []
    arr += [mask + 2] * 2
    x = 6
    for i in range(1, fill):
        arr += [x] + [x]
        x = x * 5 + 1
        x = x & mask

    arr += [1] * (n - len(arr))

    s = " ".join(map(str, arr))
    return s

def solution():
    n = int(input())
    a = [num for num in input().split()]
    c = [(int(k), v) for k, v in Counter(a).items()]
    ans = 0
    prev_v = 0
    prev_k = -1
    for k, v in sorted(c):
        if k - prev_k > 1:
            prev_v = 0
        if v > prev_v:
            ans += v - prev_v
        prev_v = v
        prev_k = k
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()