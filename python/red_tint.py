def red_tint(image_list):
    """
    Here's an example filter to give you an idea of how to approach this problem.
    """
    red_list = []
    for row in image_list:
        red_row = []
        for pixel in row:
            r, g, b = pixel
            red_row.append([255, g, b])
        red_list.append(red_row)
    return red_list
