pointsA = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
pointsB = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

with open("aoc-2022-02/input.txt", "r") as file:
    scoreA = 0
    scoreB = 0

    for line in file:
        scoreA += pointsA[line.strip("\n\r")]
        scoreB += pointsB[line.strip("\n\r")]

    print(f"Solution (part I): {scoreA}")
    print(f"Solution (part II): {scoreB}")