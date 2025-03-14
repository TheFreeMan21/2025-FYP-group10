
import random
import os
import cv2

import inpaint_util

def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False


class ImageDataLoader:
    def __init__(self, directory, shuffle=False, transform=None):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform
        i= 1179
   
        self.file_list= sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', 'jpeg', '.bmp', '.tiff')) and any(str(i) in f for i in range(1179, 1379))])

        if not self.file_list:
            raise ValueError("No image files found in the directory.")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of batches
        self.num_batches = len(self.file_list)

    def __len__(self):
        return self.num_batches

    def __iter__(self):
        #Iterating throught all the images and applying transformations if necessesary"
        for filepath in self.file_list:
            img_rgb, img_gray = readImageFile(filepath)
            blackhat, tresh, img_out = inpaint_util.removeHair(img_rgb, img_gray)

            #Save the new images on a different folder/path 
            dir_path = os.path.dirname(filepath)
            new_dir = os.path.join(dir_path, "New")
            os.makedirs(new_dir, exist_ok=True)
            saveImageFile(img_out, os.path.join(new_dir, os.path.basename(filepath)))

            if self.transform:
                img_gray= self.transform(img_gray)
                img_rgb= self.transform(img_rgb)

        return img_rgb, img_gray


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path_to_data = os.path.join(current_directory, '../data')
data_folder_path = os.path.normpath(relative_path_to_data)

Images= ImageDataLoader(data_folder_path)

Images.__iter__()