import cv2 as cv
img = cv.imread("..\\img\\photo_2023-07-31_23-02-41.jpg")


print(img)

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window

