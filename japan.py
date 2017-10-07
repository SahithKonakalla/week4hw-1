#import sys
import cv2
import numpy as np

#cap = cv2.VideoCapture(1)

img = cv2.imread("japan.png")
#img = np.asarray(img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV", img_hsv)

THRESHOLD_MIN = np.array([0, 0, 0],np.uint8)
THRESHOLD_MAX = np.array([160, 255, 255],np.uint8)

thresh = cv2.inRange(img_hsv, THRESHOLD_MIN, THRESHOLD_MAX)

cv2.imshow("Thresholded", thresh)

edges = cv2.Canny(thresh, 0, 20, 3)

cv2.imshow("Canny", edges)

(contours, _) = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,255), 3)

cv2.imshow("Done", img)