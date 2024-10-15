def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = abs(y1 - y0)
    error = dx / 2
    y_step = 1 if y0 < y1 else -1
    y = y0
    line = []
    for x in range(x0, x1 + 1):
        coord = (y, x) if steep else (x, y)
        line.append(coord)
        error -= dy
        if error < 0:
            y += y_step
            error += dx
    return line

# Начальная и конечная точки
start = (8, -2)
end = (12, 5)

# Построение отрезка
line = bresenham_line(start[0], start[1], end[0], end[1])

# Вывод последовательности смещений
movements = ""
for i in range(1, len(line)):
    if line[i][0] == line[i-1][0]:  # Горизонтальное смещение
        movements += "0"
    else:  # Диагональное смещение
        movements += "1"

print(movements)