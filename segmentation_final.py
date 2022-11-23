import numpy as np
import cv2
from sys import getsizeof
import glob
import imageio.v3 as iio
import skimage.color
import skimage.filters
from skimage.measure import regionprops

image = cv2.imread("3.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = 20
assignvalue = 255
threshold_method = cv2.THRESH_BINARY
_, result1 = cv2.threshold(gray_image,threshold,assignvalue,threshold_method)
#coords = np.column_stack(np.where(result1 == 255))
#print(coords)
#result2 = cv2.merge([result1,result1,result1])
masked = cv2.bitwise_and(image, image, mask= result1)
contours, hierarchy = cv2.findContours(result1, 1, 2)
print(getsizeof(contours))
cnt = contours[0]
perimeter = cv2.arcLength(cnt,True)
print("Perimeter is : ",perimeter)
print(result1.shape)
#print(result2.shape)
number_of_white_pix = np.sum(result1 == 255)
number_of_nonwhite_pix = np.sum(result1 < 255)
print('Number of white pixels:', number_of_white_pix)
print('Number of non white pixels:', number_of_nonwhite_pix)
print('Total Number of pixels in image:', number_of_nonwhite_pix + number_of_white_pix)
print("Area Occupied by onion in the image:", (number_of_white_pix / (number_of_nonwhite_pix + number_of_white_pix)) * 100,"percentage")
#diameter = regionprops(result1, 'MajorAxisLength')
#binary_mask = gray_image > t
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, result1)
  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
  
cv2.destroyAllWindows() 

