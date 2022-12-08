import os

import cv2
import numpy as np

#import time


def MeasureVariable():
    #start = time.time()
    img1 = cv2.imread("images/img1.jpg", 0)
    img2 = cv2.imread("images/img2.jpg", 0)
    Object = cv2.bgsegm.createBackgroundSubtractorMOG()
    mask = Object.apply(img1)
    mask = Object.apply(img2)

    cv2.imwrite("images/difference.jpg", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    difference = cv2.imread("images/difference.jpg", cv2.IMREAD_GRAYSCALE)
    whitePixels = np.count_nonzero(difference)

    os.rename("images/img2.jpg", "images/img1.jpg")

    #print("time:" + str(time.time() - start))
    return {"variable": int(whitePixels / difference.size * 100)}
