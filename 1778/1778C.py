from collections import Counter


def solution():
    n, k = (int(num) for num in input().split())
    a = input()
    b = input()
    if k >= n:
        print(n * (n + 1) // 2)
        return
    if k == 0:
        pairs = []
        streak = False
        for i, (x, y) in enumerate(zip(a, b)):
            if x == y:
                if not streak:
                    start = i
                    end = i
                    streak = True
                else:
                    end = i
            else:
                if streak:
                    pairs.append((start, end))
                    streak = False
        ans = 0
        for i, j in pairs:
            m = j - i + 1
            ans += m * (m + 1) // 2
        print(ans)
        return

    cnt = Counter()
    i = 0
    j = 0
    best = 0
    besti = 0
    bestj = 0
    while len(cnt) < k:
        if a[j] != b[j]:
            cnt[a[j]] += 1
        j += 1





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
