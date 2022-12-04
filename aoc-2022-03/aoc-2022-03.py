
def get_priority(item):
    ascii_value = ord(item)

    if ascii_value in range(65, 91):
        return ascii_value - 38
    elif ascii_value in range(97, 123):
        return ascii_value - 96
    else:
        return 0

if __name__ == '__main__':
    items = []
    badges = []

    with open("aoc-2022-03/input.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            # Part I
            length = len(line)
            halfA = line[:length//2]
            halfB = line[length//2:]
            common = set(halfA)&set(halfB)
            items.append(common.pop())

            # Part II
            if i % 3 == 0:
                badge = set(lines[i].strip())&set(lines[i+1].strip())&set(lines[i+2].strip())
                badges.append(badge.pop())


    items_total_priority = 0
    badges_total_priority = 0

    for item in items:
        items_total_priority += get_priority(item)

    for badge in badges:
        badges_total_priority += get_priority(badge)

    print(f"Solution (part I): {items_total_priority}")
    print(f"Solution (part II): {badges_total_priority}")