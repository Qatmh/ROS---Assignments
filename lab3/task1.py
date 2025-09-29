import cv2 
import numpy as np
import datetime

image = cv2.imread("images/drone_image.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


cv2.rectangle(image, (50, 50), (150, 100), (100, 200, 0), 3)
cv2.circle(image, (300, 300), 50, (255, 0, 0), 5)

points = np.array([[560, 430], [750, 430], [655, 600]])
cv2.fillPoly(image, pts=[points], color=(0, 0, 255))

cv2.putText(image, "Lassi Ahlstrand & Mahmmud Qatmh", (0, 650), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

cv2.putText(image, f"Processed: {datetime.datetime.now()}", (0, 30), 
            cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)

cv2.imshow("test", image)

cv2.waitKey(0)
cv2.destroyAllWindows()