"""
Below is the code to loop through each pixel in the picture. 
To apply a filter, we need to read the R, B, and G values from the pixel, change them in some way, and append them to our new list.

This code can be copied into the filter function as a starting point!
"""
greyscale_list = []
for row in image_list:
    grey_row = []
    for pixel in row:
        """ 
        TODO add your code here!
        1) Calculate the average of R, G, and B for the current pixel. The average will be used for the all 3 values in the new picture (this is what makes it greyscale)
        2) Append the new pixel (a list of the R, G, and B values) to the grey_row 
        """
    greyscale_list.append(grey_row)
