import cv2
image = cv2.imread('random.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_image)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedBlur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_image, invertedBlur, scale=255.0)
cv2.imwrite('sketch.png', sketch)