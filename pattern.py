for row in range(1, 10):
    if row > int(10 / 2):
        star_count = 10 - row
    else:
        star_count = row
    print("*" * star_count, end=' ')
    print()