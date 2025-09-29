import cv2 
import numpy as np


image = cv2.imread("images/wheel.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def mask_rgb(lower, upper):
    mask = cv2.inRange(image_rgb, lower, upper)
    return cv2.bitwise_and(image, image, mask=mask)

def mask_hsv(lower, upper):
    mask = cv2.inRange(image_hsv, lower, upper)
    return cv2.bitwise_and(image, image, mask=mask)


lower_red_rgb = np.array([150, 0, 0])
upper_red_rgb = np.array([255, 0, 0])

lower_green_rgb = np.array([0, 150, 0])
upper_green_rgb = np.array([80, 255, 80])

lower_blue_rgb = np.array([0, 0, 150])
upper_blue_rgb = np.array([80, 80, 255])

lower_purple_rgb = np.array([150, 0, 150])
upper_purple_rgb = np.array([255, 100, 255])

lower_cyan_rgb = np.array([0, 150, 150])
upper_cyan_rgb = np.array([80, 255, 255])

red_rgb = mask_rgb(lower_red_rgb, upper_red_rgb)
green_rgb = mask_rgb(lower_green_rgb, upper_green_rgb)
blue_rgb = mask_rgb(lower_blue_rgb, upper_blue_rgb)
purple_rgb = mask_rgb(lower_purple_rgb, upper_purple_rgb)
cyan_rgb = mask_rgb(lower_cyan_rgb, upper_cyan_rgb)

cv2.imshow("red rgb filtered", red_rgb)
cv2.imshow("green rgb filtered", green_rgb)
cv2.imshow("blue rgb filtered", blue_rgb)
cv2.imshow("purple rgb filtered", purple_rgb)
cv2.imshow("cyan rgb filtered", cyan_rgb)



lower_red1_hsv = np.array([0, 50, 70])
upper_red1_hsv = np.array([10, 255, 255])
lower_red2_hsv = np.array([170, 50, 70])
upper_red2_hsv = np.array([179, 255, 255])

lower_green_hsv = np.array([40, 50, 70])
upper_green_hsv = np.array([80, 255, 255])

lower_blue_hsv = np.array([90, 50, 70])
upper_blue_hsv = np.array([128, 255, 255])

lower_purple_hsv = np.array([140, 50, 70])
upper_purple_hsv = np.array([160, 255, 255])

lower_cyan_hsv = np.array([80, 50, 70])
upper_cyan_hsv = np.array([100, 255, 255])

red_mask = cv2.inRange(image_hsv, lower_red1_hsv, upper_red1_hsv) | cv2.inRange(image_hsv, lower_red2_hsv, upper_red2_hsv) 
red_hsv = cv2.bitwise_and(image, image, mask=red_mask)

blue_hsv = mask_hsv(lower_blue_hsv, upper_blue_hsv)
purple_hsv = mask_hsv(lower_purple_hsv, upper_purple_hsv)
green_hsv = mask_hsv(lower_green_hsv, upper_green_hsv)
cyan_hsv = mask_hsv(lower_cyan_hsv, upper_cyan_hsv)

cv2.imshow("red hsv filtered", red_hsv)
cv2.imshow("green hsv filtered", green_hsv)
cv2.imshow("blue hsv filtered", blue_hsv)
cv2.imshow("purple hsv filtered", purple_hsv)
cv2.imshow("cyan hsv filtered", cyan_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()