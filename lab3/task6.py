import cv2
import numpy as np

def concat_vh(image_list):
    return cv2.vconcat([cv2.hconcat(row) for row in image_list])

def zero_padding(image, pad_h, pad_w):
    return cv2.copyMakeBorder(image, pad_h, pad_h, 
            pad_w, pad_w, cv2.BORDER_CONSTANT, value=0)

def convolution(image, kernel):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height, width = image.shape
    kernel_height, kernel_width = kernel.shape
    pad_h = kernel_height // 2
    pad_w = kernel_width // 2

    padded = zero_padding(image, pad_h, pad_w)
    output = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            current = padded[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.sum(current * kernel)
    return output  

image = cv2.imread("images/classroom.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

gx = convolution(gray, sobel_x)
gy = convolution(gray, sobel_y)

gx = np.clip(np.abs(gx), 0, 255).astype(np.uint8)
gy = np.clip(np.abs(gy), 0, 255).astype(np.uint8)

g = np.sqrt(gx**2 + gy**2)
g = np.clip(g, 0, 255).astype(np.uint8)

grid = concat_vh([[gray, gx], 
                    [gy, g]])

grid = cv2.resize(grid, (600, 500))

cv2.imshow("original | sobel x | sobel y | combined", grid)

cv2.waitKey(0)
cv2.destroyAllWindows()