def rata_rata(data):
    if len(data) == 0:
        return "List kosong, rata-rata tidak dapat dihitung"

    total = sum(data)
    return total / len(data)


# Test case 1: 3 data
print(rata_rata([80, 90, 70]))

# Test case 2: 5 data
print(rata_rata([60, 70, 80, 90, 100]))

# Test case 3: 2 data
print(rata_rata([75, 85]))

# Test case 4: list kosong
print(rata_rata([]))