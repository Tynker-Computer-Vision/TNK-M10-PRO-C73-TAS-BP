import cv2  
import numpy as np
# Import the load_model function to load the downloaded model


# Load the model


# Load the labels


camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    

    cv2.imshow("Webcam Image", image)
 
    # Make the image a numpy array and reshape it to the models input shape.
    

    # Print original image
    

    # Normalize the image array
    
    
    # Print normalized image
    

    keyboard_input = cv2.waitKey(1)
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
