rows = [str(x) for x in range(1, 9)]
cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
board = [[col + row for col in cols] for row in rows]
volki = ["b8", "d8", "f8", "h8"]
ovza = ["a1"]
ovza_reach_upper_line = ["b8", "d8", "f8", "h8"]


def main(move, debug=False):
    global volki, ovza
    try:
        from_ = move.split()[0]
        where_ = move.split()[1]
    except:
        ValueError
        print("введите снова, что-то не так((( ")
        launcher()

    if (abs(rows.index(where_[1]) - rows.index(from_[1])) > 1 or \
        abs(cols.index(where_[0]) - cols.index(from_[0])) > 1) and debug == False:
        print("шашки не летают, введите клетки по диагонали c разницев 1 клетка")
        launcher()




    else:

        if ovza[0] == from_:
            ovza = [where_]

            for i in range(len(ovza_reach_upper_line)):
                if ovza[0] == ovza_reach_upper_line[i]:
                    print("ovza won")
                    exit()

        elif from_ in volki:
            for i in range(len(volki)):
                if from_ == volki[i]:
                    volki[i] = where_

            # ищем проигрышные для овцы положения
            if ovza[0][0] == cols[0]:
                cols_avaliable = cols[1]

            elif ovza[0][0] == cols[7]:
                cols_avaliable = cols[6]


            else:
                # print(cols[1:7])
                for i in range(len(cols)):
                    if ovza[0][0] == cols[i]:
                        # print([cols[i - 1], cols[i + 1]])
                        cols_avaliable = [cols[i - 1], cols[i + 1]]

            rows_avaliable = []

            if ovza[0][1] == rows[0]:
                rows_avaliable = rows[1]

            elif ovza[0][1] == rows[7]:
                rows_avaliable = rows[6]


            else:

                for i in range(1, len(rows)):
                    if ovza[0][1] == rows[i]:
                        rows_avaliable = [rows[i - 1], rows[i + 1]]

            res_option = [col + row for col in cols_avaliable for row in rows_avaliable]

            res_option = [sell for sell in res_option if sell not in volki and sell not in ovza]

            print(res_option)
            if res_option in volki or res_option == []:
                print("volki won")
                exit()

        else:
            print("err")


def launcher():
    while True:
        for i in cols:
            print(f"    {i}", end="")
        print("\n")
        line = 8
        for row in board[::-1]:

            print(line, end=" ")
            line -= 1
            for col in row:

                if col in volki:
                    print(f"| ⚫️|", end="")
                elif col in ovza:
                    print(f"| ⚪️|", end="")
                else:
                    print(f"|   |", end="")
            print("\n")
        move = input("введите ход : ")
        main(move, debug=True)


launcher()





