tree_data = {
    "apple": [12000, 10],
    "orange": [10000, 6],
    "mango": [27500, 15],
    "lemon": [7500, 5],
    "coconut": [8000, 15]
}

if __name__ == "__main__":
    inp = open("TOF_small.txt", "r")
    out = open("TOF_small_output.txt", "w")

    data = inp.readlines()
    r = 0

    T = int(data[r])
    r += 1

    for k in range(T):
        N, D = map(int, data[r].split())
        r += 1

        max_trees = int(N * 0.4)
        factor = []
        for key, value in tree_data.items():
            factor.append((key, (D // value[1]) * value[0]))

        factor.sort(key=lambda x: x[1], reverse=True)
        # print("Days - {0}, Total_tree -{1}, Max_tree - {2}, factor - {3}".format(D, N, max_trees, factor))

        i = 1
        total_profit = 0
        cnt = 0

        for ind, f in enumerate(factor):
            total_profit += f[1]
            cnt += 1

        # print(factor[0][0], cnt)
        while i < max_trees and cnt < N:
            total_profit += factor[0][1]
            # print(total_profit, end=' ')
            i += 1
            cnt += 1

        # print()
        # print(factor[1][0], cnt)
        i = 1
        while i < max_trees and cnt < N:
            total_profit += factor[1][1]
            # print(total_profit, end=' ')
            i += 1
            cnt += 1

        # print()
        # print(factor[2][0], cnt)
        i = 0
        # print(cnt, end=" --- ")
        while cnt < N:
            total_profit += factor[2][1]
            # print(total_profit, end=' ')
            i += 1
            cnt += 1

        # print("---", total_profit, cnt)

        out.write("Case #{0}: {1}\n".format(k + 1, total_profit))
