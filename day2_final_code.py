import numpy as np
import cv2

#APPLYING THRESHOLD ON IMAGE
image = cv2.imread("3.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = 20
assignvalue = 255
threshold_method = cv2.THRESH_BINARY
_, result1 = cv2.threshold(gray_image,threshold,assignvalue,threshold_method)

#FINDING CONTOURS
contours, hierarchy = cv2.findContours(image=result1, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)                                      
# draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

#FINDING THE LARGEST CONTOUR
c = max(contours, key = cv2.contourArea)
perimeter = cv2.arcLength(c,True)
area = cv2.contourArea(c)
print("Perimeter,area of contour is:",perimeter,area)
x,y,w,h = cv2.boundingRect(c)
print("The bounding rectangle of the largest contour is :",x,y,w,h)                
cv2.rectangle(image_copy,(x,y),(x+w,y+h),(0,255,0),2)
# see the mid results(optional)
#cv2.imshow('None approximation', image_copy)
#cv2.waitKey(0)
#cv2.imwrite('contours_none_image1.jpg', image_copy)
#cv2.destroyAllWindows()

#IMAGE MASK(SEGMENTED IMAGE)
masked = cv2.bitwise_and(image, image, mask= result1)
#OPTIONAL
print(result1.shape)

#CALCULATED VALUES
number_of_white_pix = np.sum(result1 == 255)
number_of_nonwhite_pix = np.sum(result1 < 255)
print('Number of white pixels:', number_of_white_pix)
print('Number of non white pixels:', number_of_nonwhite_pix)
print('Total Number of pixels in image:', number_of_nonwhite_pix + number_of_white_pix)
print("Area Occupied by onion in the image:", (number_of_white_pix / (number_of_nonwhite_pix + number_of_white_pix)) * 100,"percentage")
print("The area calculated by contour is approx same to this value.\nThe diameter can be found by dividing the perimeter with pi\n")
print("--------------------------------FINAL RESULT---------------------------------------\n")
print("Therefore the diameter of onion is",perimeter / 3.14," pixels")

#DISPLAYING THE IMAGE
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, image_copy)
  
#waits for user to press any key 
cv2.waitKey(0) 
  
cv2.destroyAllWindows() 

