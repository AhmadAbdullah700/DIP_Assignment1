#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


image = cv2.imread(r'C:\Users\user\Videos\data\rect1.jpg')


# In[3]:


#Convert the image to grayscale
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Apply a threshold on the grayscale image to only detect the white area
_, thresh = cv2.threshold(grayimage, 220, 255, cv2.THRESH_BINARY)

#Detect edges of the shape
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# In[4]:


for contour in contours:
    #Function used to approximate the shape
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    
    centroid_x = 0
    centroid_y = 0
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        ratio = w / h
        centroid_x = (x + x + w) / 2
        centroid_y = (y + y + h) / 2
        if ratio == 1:
            print("Square!")
        else:
            print("Rectangle!")
    else:
        print("Unknown!")
    
    perimeter = cv2.arcLength(contour, True)
    print("Perimeter: ", perimeter)
    print(f"Centroid: ({centroid_x}, {centroid_y})")


# In[5]:


#Display the image
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

