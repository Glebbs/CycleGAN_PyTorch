import glob
import io
import os
import shutil
import cv2

import numpy as np

from PIL import Image


def load_image(path_to):
    IMGS = []
    imgs_in_folder = list()
    subfolders = [f.path for f in os.scandir(path_to) if f.is_dir()]
    for folder in subfolders:
        im = [f for f in os.listdir(folder)]
        if im is not None:
            IMGS = IMGS + im
            im_f = [os.path.join(folder, f) for f in os.listdir(folder)]
            imgs_in_folder = imgs_in_folder + im_f
    return IMGS, imgs_in_folder


def from_brasile_to_one():
    # get files names, just and in the folder
    imgs, imgs_in_folder = load_image(
        '/media/vlad/20127138-1a35-451b-85c0-a84dbc12ae79/storage/gta5_2_real/cityscapes_images/val/')
    new = '/media/vlad/20127138-1a35-451b-85c0-a84dbc12ae79/storage/gta5_2_real/new_data/'

    inhg = 0
    for i in range(len(imgs)):
        shutil.copyfile(imgs_in_folder[i], os.path.join(new, imgs[i]))


from_brasile_to_one()
