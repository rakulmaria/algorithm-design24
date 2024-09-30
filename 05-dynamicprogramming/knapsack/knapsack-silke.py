from sys import stdin


def solve():
    while True:
        try:
            line = stdin.readline()
            if line == "":
                break
        except:
            break

        weights = []
        values = []

        splitted_line = line.split()
        capacity = int(splitted_line[0])
        num_objects = int(splitted_line[1])

        for i in range(num_objects):
            value, weight = stdin.readline().split()
            weights.append(int(weight))
            values.append(int(value))

        m = [[0] * (capacity + 1) for _ in range(num_objects + 1)]

        for a in range(num_objects):
            i = a + 1
            w_i = weights[a]
            v_i = values[a]
            for w in range(capacity + 1):
                before = m[a][w]
                if w_i > w:
                    m[i][w] = before
                else:
                    m[i][w] = max(before, v_i + m[a][w - w_i])

        cur_weight = capacity
        cur_obj = num_objects
        chosen_objects = []
        while True:
            cur = m[cur_obj][cur_weight]
            above = m[cur_obj - 1][cur_weight]

            if cur != above:
                chosen_objects.append(cur_obj - 1)
                cur_weight = cur_weight - weights[cur_obj - 1]

            if cur_obj <= 1:
                break
            else:
                cur_obj = cur_obj - 1

        print(len(chosen_objects))
        print(" ".join(str(e) for e in chosen_objects))


solve()
