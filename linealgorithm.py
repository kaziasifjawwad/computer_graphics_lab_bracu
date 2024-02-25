def generatePixel(x1, y1, x2, y2):
    x_list = []
    y_list = []

    # Check for vertical line
    if x1 == x2:
        y_step = 1 if y2 > y1 else -1
        for y in range(y1, y2 + y_step, y_step):
            x_list.append(x1)
            y_list.append(y)
        return x_list, y_list

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x, y = x1, y1
    x_list.append(x)
    y_list.append(y)
    for i in range(steps + 1):
        x += x_increment
        y += y_increment
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list
