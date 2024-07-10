import cv2
import numpy as np

image=cv2.imread("nodi.jpg",cv2.IMREAD_COLOR)
image=cv2.resize(image,(300,300))

# way to split in hsv format
b,g,r=cv2.split(image)
# to show diffrent color channels in BGR

#cv2.imshow('1',b)
#cv2.imshow('2',g)
#cv2.imshow('3',r)

# way to merge and see BGR combined image
image_marge=cv2.merge((b,g,r))
cv2.imshow('4',image_marge)
# to conver BGR to RGB format
img_rgb=cv2.cvtColor(image_marge,cv2.COLOR_BGR2RGB)
cv2.imshow('5',img_rgb)
#to convert BGR to HSV format
img_hsv=cv2.cvtColor(image_marge,cv2.COLOR_BGR2HSV)
cv2.imshow('6',img_hsv)
# way to split in hsv format
h,s,v =cv2.split(img_hsv)
#to show diffrent HSV channles 

#cv2.imshow('7',h)
#cv2.imshow('8',s)
#cv2.imshow('9',v)

#modification of h,s,v channels
h_1=h+20
s_1=s+20
v_1=v-10
#marged image after modification of hsv channels
img_modi=cv2.merge((h_1,s_1,v_1))
#convert hsv to RGB
img_modi_rgb=cv2.cvtColor(img_modi,cv2.COLOR_HSV2RGB)
cv2.imshow('10',img_modi)
cv2.imshow('10',img_modi_rgb)

#cv2.imshow('new',image)
#to save in desktop or directory you can use this function

#cv2.imwrite("name you want to give to the file ", img_modi_rgb )

cv2.waitKey(123430)
cv2.destroyAllWindows()
