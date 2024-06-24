import cv2 as cv
import numpy as np

if __name__ == "__main__":
    nameDepth  = './robolab/video1/depth_image1.png'
    nameRGB = './robolab/video1/color_image1.png'

    img_depth = cv.imread(nameDepth, cv.IMREAD_ANYDEPTH)
    img_rgb = cv.imread(nameRGB)

    print(np.shape(img_depth))
    print(np.shape(img_rgb))

    #img_depth = np.array(cv.imread(nameDepth), dtype=np.float32)
    print(img_depth.min(), img_depth.max())
    img_depth = np.array(img_depth, dtype=np.float32)

    print(type(img_depth[0][0]))
    print(type(cv.imread(nameDepth)))

