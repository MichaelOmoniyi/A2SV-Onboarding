t = int(input())

for _ in range(t):
    n = int(input())

    if n <= 2:
        print(0)
    else:
        if n % 2 == 0:
            print(n - ((n + 2) // 2))
        else:
            print(n - ((n + 1) // 2))