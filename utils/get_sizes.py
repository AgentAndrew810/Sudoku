def get_sizes(screen_width: int, screen_height: int) -> dict[str:int]:
    # if the width is bigger than the ratio, use the height to calculate the width
    if screen_width >= screen_height * 5 // 4:
        height = screen_height
        width = round(height * 5 / 4)
    # otherwise use the width to calculate height
    else:
        width = screen_width
        height = round(width * 4 / 5)

    # use the height and width to calculate other sizes
    padd = round(width / 25)
    cell_size = padd * 2
    board_size = cell_size * 9
    font = round(cell_size * 0.8)
    line_size = max(1, round(cell_size / 64))
    big_line_size = line_size * 4

    # calculate the x_padd and y_padd based on if the height or width was adjusted
    x_padd = padd + (screen_width - width) // 2
    y_padd = padd + (screen_height - height) // 2

    return {
        "cell_size": cell_size,
        "board_size": board_size,
        "x_padd": x_padd,
        "y_padd": y_padd,
        "padd": padd,
        "font_size": font,
        "line_size": line_size,
        "big_line_size": big_line_size,
    }
