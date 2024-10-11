def initialize():
    days = ["0"*20 for i in range(1, 7)]
    return days


def start_point(text):
    start_height = 0
    for i in text:
        if "ming" in i[1]:
            start_height = i[0][0][1]
            break
    return start_height


def sort_row(text):
    rows = []
    text.sort()
    cmp = text[0][0][0][0]
    current_row = []
    for i in range(0, len(text)):
        if (cmp - 20)<= text[i][0][0][0] <= (cmp + 20):
            current_row.append(text[i])
        else:
            cmp = text[i][0][0][0]
            rows.append(current_row)
            current_row = [text[i]]
    rows.append(current_row)
    return rows


def column(start_height, cell_height, corners):
    return int((corners[0][1] - start_height)/cell_height) - 2


def mean_height(lists):
    s = 0
    for i in lists:
        s += i
    return int(s/len(lists))


def mean_cell_height(text):
    text.sort(key=lambda a: a[0][0][1])
    heights = []
    for i in range(1, len(text) - 1):
        a = (text[i + 1][0][3][1] + text[i + 1][0][0][1])/2
        b = (text[i][0][3][1] + text[i][0][0][1])/2
        h = a - b
        heights.append(h)
    mean = mean_height(heights)
    return mean


def alter(s, index, no_of_char):
    x = list(s)
    for i in range(index, index + no_of_char):
        x[i] = "1"
    s1 = "".join(x)
    return s1


def spl_char(s):
    if "@Lab" in s:
        return 4, False
    elif "Lab" in s:
        return 4, True
    elif "@" in s:
        return 2, True
    return 2, False


def assign(s, day_schedule, start_height, cell_height):
    for i in day_schedule:
        col = column(start_height, cell_height, i[0])
        if col < 0:
            continue
        elif col <= 3:
            no_of_chars, shift = spl_char(i[1])
            index = col * 2
            if shift:
                s = alter(s, index + 1, no_of_chars)
            else:
                s = alter(s, index, no_of_chars)
        else:
            no_of_chars, shift = spl_char(i[1])
            index = (col * 2) + 1
            if shift:
                s = alter(s, index + 1, no_of_chars)
            else:
                s = alter(s, index, no_of_chars)
    return s


def assign_loop(tt, days, start_height, cell_height):
    for i, j in enumerate(days):
        tt[i] = assign(tt[i], j, start_height, cell_height)


def assign_ipd(tt):
    for i, j in enumerate(tt):
        if i is "0"*20:
            tt[j] = "1"*20
            break

