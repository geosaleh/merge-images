# @PY4ALL

import cv2
import numpy as np

def merge_h(im1, im2):
    im1_shape = np.shape(im1)
    im2_shape = np.shape(im2)
    if im1_shape[0] < im2_shape[0]:
        im1 = np.pad(im1, ((0, im2_shape[0] - im1_shape[0]), (0, 0), (0, 0)), mode='edge')
    else:
        im2 = np.pad(im2, ((0, im1_shape[0] - im2_shape[0]), (0, 0), (0, 0)), mode='edge')

    im_out = np.hstack((im1,im2))
    cv2.imwrite('out_file_h.png',im_out)


def merge_v(im1, im2):
    im1_shape = np.shape(im1)
    im2_shape = np.shape(im2)
    if im1_shape[1] < im2_shape[1]:
        im1 = np.pad(im1, ((0, 0), (0, im2_shape[1] - im1_shape[1]), (0, 0)), mode='edge')
    else:
        im2 = np.pad(im2, ((0, 0), (0, im1_shape[1] - im2_shape[1]), (0, 0)), mode='edge')
    im_out = np.vstack((im1,im2))
    cv2.imwrite('out_file_v.png',im_out)


im1 = cv2.imread("image1.png")
im2 = cv2.imread("image2.png")
merge_h(im1, im2)
merge_v(im1, im2)


