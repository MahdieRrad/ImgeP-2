import cv2
import numpy as NumPy
imge = NumPy.arange(0, 122500, 1, NumPy.uint8)
imge = NumPy.reshape(imge, (350,350))
imge[:,:] = 0
                
imge[110:140,110:200]=255                                #khat bala  M
imge[110:200,150:170]=255                                #khat vast M
imge[110:200,100:120] =255                           #khat samt Chap M
imge[110:200,200:220] =255                          #Khat Samt Rast M


cv2.imshow('Type M',imge)
cv2.waitKey()
