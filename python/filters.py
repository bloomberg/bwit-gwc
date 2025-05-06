def greyscale(image_list):
    """
    Apply a greyscale filter to the image.
    """
    greyscale_list = []
    for row in image_list:
        grey_row = []
        for pixel in row:
            # Calculate the average of R, G, and B for the current pixel
            grey_value = sum(pixel) // 3
            # Assign the grey value to all three channels (R, G, B)
            grey_row.append([grey_value, grey_value, grey_value])
        greyscale_list.append(grey_row)
    return greyscale_list
