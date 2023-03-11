if __name__ == "__main__":
    inp = open("ET_small.txt", "r")
    out = open("ET_small_output.txt", "w")

    data = inp.readlines()
    r = 0

    T = int(data[r])
    r += 1

    ans = []

    for i in range(T):
        townships = int(data[r])
        r += 1

        total_walls = 0
        for _ in range(townships):
            N, R, S, H = map(int, data[r].split(','))
            r += 1
            total_walls += (H * 6) + ((S + R) * 3) + S

        accent_walls = total_walls / 3
        # (accent_walls * 2.5) + ((total_walls - accent_walls) * 3.25)
        total_hours = total_walls * 3
        accent_qty = accent_walls * 1.5
        regular_qty = (total_walls - accent_walls) * 2.25

        total_hours = round(total_hours, 3)
        accent_qty = round(accent_qty, 3)
        regular_qty = round(regular_qty, 3)

        ans.append((i, total_hours, accent_qty, regular_qty))

    for x, hours, accent, reqular in ans:
        out.write("Case #{3}: {0:.2f}, {1:.2f}, {2:.2f}\n".format(
            hours, accent, reqular, x+1))
