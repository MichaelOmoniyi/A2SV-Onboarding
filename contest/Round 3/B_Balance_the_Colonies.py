t = int(input())

for _ in range(t):
    n = int(input())

    if n <= 3:
        print(n)
    else:
        colonyA = n // 2
        colonyB = n - colonyA

        print(max(colonyA, colonyB) - min(colonyA, colonyB))