import cv2
import numpy as np
image =cv2.imread('nodi.jpg')
image=cv2.resize(image,(300,300))

#form filters
kernal_identity=np.array([[0,0,0],[0,1,0],[0,0,0]])
kernal_3=np.ones((3,3), dtype=np.float32) /9.0
kernal_11=np.ones((11,11), dtype=np.float32) /121.0

#apply filters
output1=cv2.filter2D(image,-1,kernal_identity)
output2=cv2.filter2D(image,-1,kernal_3)
output3=cv2.filter2D(image,-1,kernal_11)

#show the results

cv2.imshow('Original',image)
cv2.imshow('Identity',output1)
cv2.imshow('3x3',output2)
cv2.imshow('11x11',output3)
cv2.waitKey(123432)
cv2.destroyAllWindows()

