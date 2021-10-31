#Grdnt

import cv2 
import numpy as NumPy

imge=NumPy.arange(0,90000,1,NumPy.uint8)
imge=NumPy.reshape(imge,(300,300))
Width,Height = imge.shape


for i in range(Width):
    imge[i:i+1,:]=255-i

cv2.imshow('Gradint ',imge)
cv2.waitKey()
