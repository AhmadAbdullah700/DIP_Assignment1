#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


def hair_length(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #Canny edge detection
    edges = cv2.Canny(gray, threshold1=200, threshold2=200 * 2)
    cv2.imshow('Result', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #Seperate all the detected shapes 
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #Calculate the perimeter of the hair
    max_length = 0
    for contour in contours:
        perimeter = cv2.arcLength(contour, closed=True)
        if perimeter > max_length:
            max_length = perimeter

    return max_length


# In[3]:


left_image = r"C:\Users\user\Videos\data\fig3.jpg"
right_image = r"C:\Users\user\Videos\data\fig4.jpg"

#Calculate the length of the hair
hair_length_right = hair_length(right_image)
hair_length_left = hair_length(left_image)

# Compare hair lengths to make the gender determination
if hair_length_left > hair_length_right:
    print("The left image is most likely a girl.")
elif hair_length_left < hair_length_right:
    print("The right image is most likely a girl.")
elif hair_length_left == hair_length_right:
    print("Both images are the same.")

