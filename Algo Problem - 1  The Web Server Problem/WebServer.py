if __name__ == "__main__":
    inp = open("TWSP_large.txt", "r")
    out = open("TWSP_large_output.txt", "w")
    data = inp.readlines()
    r = 0
    T = int(data[r])
    r += 1
    ans = []
    for _ in range(T - 1):
        A, B, C = map(int, data[r].split())
        r += 1

        ans.append((A, B, C))
        ans.sort(key=lambda p: (p[0], -p[1], p[2]))

    for a, b, c in ans:
        out.write("{0},{1},{2}\n".format(a, b, c))
