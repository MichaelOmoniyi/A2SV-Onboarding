t = int(input())

for _ in range(t):
    n = input()
    friends = list(map(int, input().split(" ")))
    friendsSum = sum(friends)
    count = 0

    if friendsSum % len(friends) == 0:
        for friend in friends:
            if friend > (friendsSum / len(friends)):
                count += 1
        print(count)
    else:
        print(-1)
    