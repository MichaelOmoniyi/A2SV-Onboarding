t = int(input())

for _ in range(t):
    n = int(input())
    targets = list(map(int, input().split(" ")))
    uniqueTarget = set()

    for target in targets:
        uniqueTarget.add(target)

    print((len(uniqueTarget) - 1) + len(uniqueTarget))