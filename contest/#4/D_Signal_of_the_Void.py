t = int(input())

for _ in range(t):
    # Read n (hubs) and p (Earth cost)
    n, p = list(map(int, input().split()))

    # a: capacities, b: costs
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Combine and sort by relay cost (b_i)
    hubs = []
    for i in range(n):
        if b[i] < p:
            hubs.append((b[i], a[i]))

    hubs.sort()

    # Initial cost: Earth must beam to at least one hub
    total_cost = p
    total_reached = 1

    for cost_relay, capacity in hubs:
        if total_reached >= n:
            break

        # How many more people do we need to reach?
        needed = n - total_reached
        # How many can this specific hub reach?
        can_reach = min(capacity, needed)

        total_cost += can_reach * cost_relay
        total_reached += can_reach

    # If some hubs are still not reached, they must be reached via Earth
    if total_reached < n:
        total_cost += (n - total_reached) * p

    print(total_cost)