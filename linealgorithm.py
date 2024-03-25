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

def generatePixelForCircle(radius, xc, yc):
    x_list = []
    y_list = []

    x = radius
    y = 0
    d = 1 - radius

    append_points(x, y, xc, yc, x_list, y_list)

    while x > y:
        if d < 0:
            d += 2 * y + 3
        else:
            d += 2 * (y - x) + 5
            x -= 1
        y += 1
        append_points(x, y, xc, yc, x_list, y_list)

    return x_list, y_list

def append_points(x, y, xc, yc, x_list, y_list):
    x_list.extend([x + xc, -x + xc, x + xc, -x + xc, y + xc, -y + xc, y + xc, -y + xc])
    y_list.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])
