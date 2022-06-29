import cv2
from cv2 import IMWRITE_JPEG2000_COMPRESSION_X1000
from numpy import imag

im = cv2.imread(r'C:\Users\HP-PC\OneDrive\Desktop\python\multimedia\sample_sample.jpeg')
print(im.shape)
cv2.imshow('Image window', im)  ## to show the image
cv2.waitKey(0)   ### to stop the display window