import cv2
import numpy as np
from matplotlib import pyplot as plt

def display_image(image, title, subplot_position):
    plt.subplot(3, 3, subplot_position)
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

def bit_plane_slice(image):
    # Get the height and width of the image
    height, width = gray_image.shape
    # Initialize an empty list to store bit planes
    bit_planes = []
    # Perform bit plane slicing
    for i in range(8):
        # Extract the i-th bit plane
        bit_plane = (gray_image >> i) & 1
        bit_planes.append(bit_plane)
    # Display original and bit plane sliced images
    display_image(image, 'Original Image', 1)
    for i, bit_plane in enumerate(bit_planes):
        display_image(bit_plane * 255, f'Bit Plane {i}', i + 2)  # Scale to 0-255 for display

# Load the image
image_path = "C:\\Users\\petra\\Downloads\\Bit_slicing.jpg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if image is None:
    print("Error: Image not found or unable to read the image.")
else:
    bit_plane_slice(image)
    plt.tight_layout()
    plt.show()
 
