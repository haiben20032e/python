import cv2
import numpy as np
#reading the image
image = cv2.imread('e:/a.jpg')

#dividing height and with by 2 to get the center of the image
height, width = image.shape[:2]
# get tx and ty values for translation
# you can specify any value of your choice 
tx, ty = width / 4, height / 4
# create the translation matrix using tx and ty, it is a NumPy array
translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty]
], dtype=np.float32)
# apply the translation to the image 
translated_image =cv2.warpAffine(src=image,M=translation_matrix, dsize=(width, height))
# display the original and the Translated images
cv2.imshow('Translated image', translated_image)
cv2.imshow('Original image', image)
cv2.waitKey(0)
# save the translated image to disk
cv2.imwrite('translated_image.jpg', translated_image)