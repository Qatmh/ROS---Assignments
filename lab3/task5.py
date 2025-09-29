import numpy as np 
import cv2

def box_blur(size):
    return np.ones((size, size), np.float32) / (size * size)

def zero_padding(image, pad):
    return cv2.copyMakeBorder(image, pad, pad, 
            pad, pad, cv2.BORDER_CONSTANT, value=0)

def convolution(image, kernel):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = image.shape
    kernel_height, kernel_width = kernel.shape
    pad = kernel_height // 2

    padded = zero_padding(image, pad)
    output = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            current = padded[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.sum(current * kernel)
    return output            


image = cv2.imread("images/flower.png")

for size in [3, 5, 11]:
    kernel = box_blur(size)
    blurred = convolution(image, kernel)
    cv2.imshow(f"blurred {size}x{size}", blurred)

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow(f"gaussian 5x5", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()