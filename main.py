import sys
import os
sys.path.append(os.path.abspath("util"))

from os.path import join

import matplotlib.pyplot as plt

from util.img_util import  saveImageFile
from util.img_util import readImageFile
from util.inpaint_util import removeHair


import os

file_path = os.path.abspath(os.path.join(os.getcwd(), "data", "example.jpg"))

current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path_to_data = os.path.join(current_directory, './result')
data_folder_path = os.path.normpath(relative_path_to_data) #save directory for the output


# read an image file
img_rgb, img_gray = readImageFile(file_path)

# apply hair removal
blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=5, threshold=10)

# plot the images
plt.figure(figsize=(15, 10))

# original image
plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# blackHat image
plt.subplot(2, 2, 2)
plt.imshow(blackhat, cmap="gray")
plt.title("BlackHat Image")
plt.axis("off")

# thresholded mask
plt.subplot(2, 2, 3)
plt.imshow(thresh, cmap="gray")
plt.title("Thresholded Mask")
plt.axis("off")

# inpainted image
plt.subplot(2, 2, 4)
plt.imshow(img_out)
plt.title("Inpainted Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# save the output image
save_file_path = join(data_folder_path, 'output.jpg')
saveImageFile(img_out, save_file_path)
