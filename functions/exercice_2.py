def get_odds():
    return [i for i in range(1, 10) if i % 2 != 0]


position = 1
for i in get_odds():
    if position == 3:
        print(i)
    position += 1
