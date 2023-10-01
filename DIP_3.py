#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def blurred(image_original, image_blurred):
    original_image = cv2.imread(image_original, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.imread(image_blurred, cv2.IMREAD_GRAYSCALE)

    #Calculate variance for both images
    variance_original = np.var(original_image)
    variance_blurred = np.var(blurred_image)

    #Image with lower variance is blurred
    if variance_blurred > variance_original:
        return "Blurred Image", "Original Image"
    else:
        return "Original Image", "Blurred Image"


# In[3]:


image_original = r"C:\Users\user\Videos\data\fig5.jpg"
image_blurred = r"C:\Users\user\Videos\data\fig5_blur.jpg"

title1, title2 = blurred(image_original, image_blurred)

original_image = cv2.imread(image_original)
blurred_image = cv2.imread(image_blurred)

cv2.imshow(title1, original_image)
cv2.imshow(title2, blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

