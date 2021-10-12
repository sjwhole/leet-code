def fractional_knapsack(cargo):
    capacity = 15
    pack = []
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    ans = 0
    for p in pack:
        if capacity >= p[2]:
            capacity -= p[2]
            ans += p[1]
        else:
            ans += capacity * p[0]
            break
    return ans


if __name__ == "__main__":
    cargo = [
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2),
    ]
    print(fractional_knapsack(cargo))
