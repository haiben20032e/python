import cv2
#reading the image
image = cv2.imread('e:/a.jpg')

#dividing height and with by 2 to get the center of the image
height, width = image.shape[:2]
#get the center cỏodinates of the image to create the 20 rotation matrix 
center =(width/2, height/2)

#using cv2.getRotationMatrix2D() to gẻ the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)

#rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotated_image)
#wait indefinitely, press any key on keybỏad to exit
cv2.waitKey(0)
#save the rotated image to disk
cv2.imwrite('rotated_image.jpg', rotated_image)