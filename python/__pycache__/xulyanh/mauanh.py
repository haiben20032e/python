import cv2
import numpy
img = cv2.imread('E:/khung_hinh/fram/4.jpg') 
blue, green, red = cv2.split(img)
zeros = numpy.zeros(blue.shape, numpy.uint8)
blueBGR =cv2.merge((blue,zeros, zeros)) 
greenBGR= cv2.merge((zeros, green, zeros))
redBGR = cv2.merge((zeros, zeros, red))
cv2.imshow('Anh ban dau', img) 
cv2.imshow('blue BGR', blueBGR)
cv2.imshow('green BGR', greenBGR)
cv2.imshow('red BGR', redBGR)
cv2.waitKey(0)
cv2.destroyAllwindows()