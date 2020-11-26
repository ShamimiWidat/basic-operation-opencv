import cv2
import numpy as np

#using numpy is faster
image = cv2.imread("nisekoi_chitoge.png")
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#output the bgr pixels
print("image")
print(image)
print("gray scale")
print(image_grayscale)

#ouput the size of picture
print(image.shape)
rows, cols, ch = image.shape

#take region of interest of the picture starting from which row and column
#roi = image[0:rows,0:cols]<<if all
roi = image[300:600,300:600]

#output the bgr pixels at specific location of picture's pixels
print(image[100,100])

#for gray scale, 0 = black, 255  white
image_grayscale[200,200] = 255

#change the specific pixel to blue
image[100,100] = (255, 0, 0)
image[100,101] = (255, 0, 0)
image[100,102] = (255, 0, 0)
image[100,103] = (255, 0, 0)
image[100,104] = (255, 0, 0)

cv2.imshow("chitoge", image)
cv2.imshow("gray picture", image_grayscale)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

#grayscale only have one channel, color 3 channel for every pixel
