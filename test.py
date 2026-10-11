import cv2
import numpy as np

image = cv2.imread("image.png")

# Use a wider datatype to avoid uint8 overflow
temp = image.astype(np.int16) + 40

brighter = np.clip(temp, 0, 255).astype(np.uint8)

darker = np.clip(
    image.astype(np.int16) - 80,
    0, 255
).astype(np.uint8)

cv2.imwrite("brighter.jpg", brighter)
cv2.imwrite("darker.jpg", darker)