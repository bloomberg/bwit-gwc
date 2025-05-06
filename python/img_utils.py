from PIL import Image
from typing import List

# Define a custom type alias for image_list

Pixel = List[int] # A list intended to have 3 integers (R, G, B)
ImageList = List[List[Pixel]]  # A 2D list of pixels, where each pixel is a list of 3 integers (R, G, B)

class ImageProcessor:
    def __init__(self):
        self.dimensions = (0, 0)

    def load_image(self, image_path: str) -> ImageList:
        """
        Load an image and convert it to a 2D list of RGB values.

        Args:
            image_path (str): Path to the input image.

        Returns:
            ImageList: A 2D list of RGB values.
        """
        img = Image.open(image_path)
        img.show()
        img = img.convert("RGB")  # Ensure image is in RGB format

        width, height = img.size
        self.dimensions = (width, height)  # Store dimensions in the class state
        data = list(img.getdata())
        return [[[r, g, b] for r, g, b in data[i * width:(i + 1) * width]] for i in range(height)]

    def save_image(self, image_list: ImageList, output_path: str) -> Image.Image:
        """
        Save a 2D list of RGB values as an image.

        Args:
            image_list (ImageList): 2D list of RGB values.
            output_path (str): Path to save the output image.

        Returns:
            Image.Image: The saved image object.
        """
        # Flatten the 2D list back into a 1D list for Pillow
        flat_list = [tuple(pixel) for row in image_list for pixel in row]
        img = Image.new("RGB", self.dimensions)
        img.putdata(flat_list)
        img.save(output_path)
        return img

    def show_image(self, image_list: ImageList) -> None:
        """
        Display a 2D list of RGB values as an image.

        Args:
            image_list (ImageList): 2D list of RGB values.
        """
        flat_list = [tuple(pixel) for row in image_list for pixel in row]
        img = Image.new("RGB", self.dimensions)
        img.putdata(flat_list)
        img.show()
