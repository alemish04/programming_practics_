import random
from random import randint

rows = [str(x) for x in range(1, 9)]
cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
board = [[col + row for col in cols] for row in rows]
for row in board:
    print(row)
# white - Black a1
f = 1  # white
color = {}
for row in board:
    for col in row:
        if f == 1:
            color[col] = "W"
            f = 0
        else:
            color[col] = "B"
            f = 1

print(color)

volki = ["b8", "d8", "f8", "h8"]
ovza = ["a1"]
current_pos = []
current_pos.append(volki)
current_pos.append(ovza)
print(current_pos)


def make_move(current_pos, color_):
    global ovza, volki
    volki = current_pos[0]
    ovza = current_pos[1]

    cols_avaliable = ''

    if color_ == "W":
        ###############################################
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

        # print(cols_avaliable)

        #######################################
        rows_avaliable = []

        if ovza[0][1] == rows[0]:
            rows_avaliable = rows[1]

        elif ovza[0][1] == rows[7]:
            rows_avaliable = rows[6]


        else:

            for i in range(1, len(rows)):
                if ovza[0][1] == rows[i]:
                    rows_avaliable = [rows[i - 1], rows[i + 1]]

        # print(rows_avaliable)

        res_option = []

        for i in cols_avaliable:
            for j in rows_avaliable:
                res_option.append(i + j)

        # print(res_option)
        for sell in res_option:
            if sell in volki or sell in ovza:
                res_option.remove(sell)
        if res_option == []:
            print("volki won")
            exit()
        else:

            new_cell = random.randint(0, len(res_option) - 1)
            # better_num = str(max([i[1] for i in res_option]))
            # for i in res_option:
            #     if better_num in i:
            #         new_cell=i

            ovza = [res_option[new_cell]]
            print(ovza)
    else:

        def volki_move(choose_volk):
            nonlocal volki_free
            # print(volki)
            # choose_volk = random.randint(0, len(volki) - 1)

            volk = volki[choose_volk]
            cols_avaliable = []
            # print(volk)

            if volk[0] == cols[0]:
                cols_avaliable = cols[1]

            elif volk[0] == cols[7]:

                cols_avaliable = cols[6]

            else:
                for i in range(len(cols)):
                    if volk[0] == cols[i]:
                        # print([cols[i - 1], cols[i + 1]])
                        cols_avaliable = [cols[i - 1], cols[i + 1]]

            rows_avaliable = []
            # print(volk[1], rows[0])
            if volk[1] == rows[0]: # нужно тормознуть волка, когда он дошёл до края доски

                rows_avaliable = []

            elif volk[1] == rows[7]:
                rows_avaliable = rows[6]


            else:

                for i in range(1, len(rows)):
                    if volk[1] == rows[i]:
                        rows_avaliable = [rows[i - 1]]

            res_option = []  # current volk's options

            res__option = []
            if rows_avaliable==[]:
                pass

            else:
                for i in cols_avaliable:
                    for j in rows_avaliable:
                        res_option.append(i + j)

                # print(res_option) какая-то проблема, тут массив с доступыми ячейками может быть пустым.
                for op in range(len(res_option)):
                    # print("\n\n\n\n\ncheck+++", volki, ovza, res_option, "\n\n\n\n")
                    if res_option[op] in volki or res_option[op] in ovza:
                        pass
                    else:
                        res__option.append(res_option[op])
                        # res_option.remove(res_option[op])
                        # # res_option = [x for x in res_option if x != op]
                        # print("dell^", res_option)

            if res__option != []:
                volki_free[choose_volk] = res__option

        # волки ходят, далее нужно понять, может ли каждый из волков ходить
        volki_free = {}
        for i in range(len(volki)):
            # print(volki_free)
            volki_move(i)

        # print("волки : ", volki_free)

        def move(volki_free):
            global volki
            print("volki_____freee", volki_free)
            # random_volk = random.randint(0, len(volki_free.keys()) - 1)  # number of volk chosen
            # print(random_volk)
            if list(volki_free.keys())==[]:
                print("волкам некуда ходить типа")
                print("овца победила")
                exit()
            else:
                random_volk = random.choice(list(volki_free.keys()))
                # print("пооооооооо", llll)
                # random_volk=volki_free[llll]
                print("random volk----", random_volk)
                volki[random_volk] = volki_free[random_volk][0]

        move(volki_free)


last_color = "B"
for i in range(1000):
    current_pos = []
    current_pos.append(volki)
    current_pos.append(ovza)
    if last_color == "B":

        make_move(current_pos, "W")
        last_color = "W"
        pass
    else:
        print("move ^ ", i)

        make_move(current_pos, "B")
        print("posssssss", volki, ovza)
        # last_color = "B"
        for ih in volki:
            if volki.count(ih) == 2:
                print("error")
                exit()
        last_color="B"
