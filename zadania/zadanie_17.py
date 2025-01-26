import math

def xy_from_colrow(col, row, x_min, y_max, x_res, y_res):
    
    x = x_min + (col + 0.5) * x_res
    y = y_max - (row + 0.5) * y_res
    return x, y

def colrow_from_xy(x, y, x_min, y_max, x_res, y_res):
    
    col = math.floor((x - x_min) / x_res)
    row = math.floor((y_max - y) / y_res)
    return col, row

xy_from_colrow(60, 12, 0, 100, 10, 10)

colrow_from_xy(48, 95, 0, 100, 10, 10)

