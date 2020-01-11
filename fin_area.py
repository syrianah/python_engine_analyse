# http://www.space-rockets.com/arsainfo.html#finsize


def fin_area(diameter, lenght):
    return round(0.13 * ((diameter + 0.5) * lenght), 2)


def fin_width(diameter):
    return round(1.25 * diameter, 2)


def calculate_fin(fin_area, fin_width):
    tg70 = 2.7475
    tg35 = 0.7002
    x = fin_width / tg70
    y = fin_width / tg35
    z = fin_area / fin_width - x / fin_width - y / fin_width
    fin_length = x + y + z
    return {"fin_x": x, "fin_y": y, "fin_z": z, "fin_length": fin_length, "fin_width": fin_width, "fin_area": fin_area}


diameter = 75.5
length = 1500

fin = calculate_fin(fin_area(diameter, length), fin_width(diameter))
print(fin)
