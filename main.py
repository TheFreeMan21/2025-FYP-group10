import sys
import os
sys.path.append(os.path.abspath("util"))

from os.path import join

import matplotlib.pyplot as plt

from util.img_util import  saveImageFile
from util.img_util import readImageFile as read_img
from util.inpaint_util import removeHair


import os

file_path = os.path.abspath(os.path.join("..", "data", "example.jpg"))


save_dir = os.path.abspath(os.path.join("..", "result"))

# read an image file
img_rgb, img_gray = read_img(file_path)

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
save_file_path = join(save_dir, 'output.jpg')
saveImageFile(img_out, save_file_path)
