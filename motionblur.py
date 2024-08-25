import cv2
import numpy as np
image =cv2.imread('nodi.jpg')
image=cv2.resize(image,(500,500))
size=25
kernal = np.zeros((size,size))
kernal[int((size-1)/2),:]=np.ones(size)
kernal=kernal/size

output=cv2.filter2D(image,-1,kernal)

cv2.imshow('image',output)
cv2.waitKey(123430)