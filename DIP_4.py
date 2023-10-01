#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


def calculate_area_centroid(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresholded = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3)

    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    centroid_x = 0
    centroid_y = 0
    
    for contour in contours:
        area = cv2.contourArea(contour)
        print("Area: ", area)
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        x, y, w, h = cv2.boundingRect(approx)
        centroid_x = (x + x + w) / 2
        centroid_y = (y + y + h) / 2
        print("Centroid: ", centroid_x, centroid_y)


# In[3]:


image_path = r"C:\Users\user\Videos\data\fig1.jpg"  # Replace with the path to your image

calculate_area_centroid(image_path)

image = cv2.imread(image_path)

#Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

