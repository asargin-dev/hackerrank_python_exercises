if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])

    scores = [v for _, v in records]

    second_min = list(sorted(set(scores)))[1]

    for j in sorted([i for i, v in records if v == second_min]):
        print(j)
