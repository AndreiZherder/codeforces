


def solution():
    n = int(input())
    points1, points2, points3 = 0, 0, 0
    words1 = set(input().split())
    words2 = set(input().split())
    words3 = set(input().split())

    union123 = words1 & words2 & words3
    words1 -= union123
    words2 -= union123
    words3 -= union123

    union12 = words1 & words2
    points1 += len(union12)
    points2 += len(union12)
    words1 -= union12
    words2 -= union12

    union13 = words1 & words3
    points1 += len(union13)
    points3 += len(union13)
    words1 -= union13
    words3 -= union13

    union23 = words2 & words3
    points2 += len(union23)
    points3 += len(union23)
    words2 -= union23
    words3 -= union23

    points1 += 3 * len(words1)
    points2 += 3 * len(words2)
    points3 += 3 * len(words3)

    print(points1, points2, points3)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
