import cv2

trainer_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')





"""
# code to detect faces from an image

#choose an image to detect faces
img = cv2.imread('srk.jpg')
#to convert the image to grayscale
grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#compares all the images with our image and then gives us the coordinates
face_coordinates = trainer_face_data.detectMultiScale(grayscaled_img)
#to show an image
for (x,y,w,h) in face_coordinates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('My Face Detector App',img)
#to pause the execution until a key is pressed so the photo doesn't close on its own
cv2.waitKey()
"""

"""
#Code to detect image from video
#webcam or video selected to scan images
video = cv2.VideoCapture('video.mp4')
#to repeteadelty keep scanning the window
while True:
    #to read the current frame
    successful_frame_read,frame = video.read()
    #to convert the image to grayscale
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #compares all the images with our image and then gives us the coordinates
    face_coordinates = trainer_face_data.detectMultiScale(grayscaled_img)
    #to automatically assign x and y coordinates from the face_coordinates array of arrays
        #draw rectangle 
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow('My Face Detector App',frame)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break   
"""





#Code to detect image during webcam
#webcam or video selected to scan images
webcam = cv2.VideoCapture(0)
#to repeteadelty keep scanning the window
while True:
    #to read the current frame
    successful_frame_read,frame = webcam.read()
    #to convert the image to grayscale
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #compares all the images with our image and then gives us the coordinates
    face_coordinates = trainer_face_data.detectMultiScale(grayscaled_img)
    #to automatically assign x and y coordinates from the face_coordinates array of arrays
        #draw rectangle 
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow('My Face Detector App',frame)
    key = cv2.waitKey(2)
    if key==81 or key==113:
        break   
webcam.release()

print("Code Completed")
