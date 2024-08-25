import cv2
import numpy as np
image =cv2.imread('noise.jpg')
image=cv2.resize(image,(500,500))
rows,col=image.shape[:2]
#kernek blurring usning filter2D
kernel_25=np.ones((25,23),np.float32)/625.0
output1=cv2.filter2D(image,-1,kernel_25)
#box filter & blur function
output_blur=cv2.blur(image,(25,25))
output_box=cv2.boxFilter(image,-1,(5,5),normalize=False)
#gaussian blur
output_gaussian=cv2.GaussianBlur(image,(5,5),0)
#median blur to reduction nosie
output_median=cv2.medianBlur(image,5)
#bilateral filter (reduction + preserving od edges)
output_bilateral=cv2.bilateralFilter(image,5,7,7)

cv2.imshow('original',image)
cv2.imshow('new',output1)
cv2.imshow('new1',output_blur)
cv2.imshow('new2',output_box)
cv2.imshow('new3',output_gaussian)
cv2.imshow('new4',output_median)
cv2.imshow('new5',output_bilateral)
cv2.waitKey(10987656)
