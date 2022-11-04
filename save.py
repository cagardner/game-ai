from PIL import ImageGrab   #pip install image
import cv2  #pip install opencv-ptyhon
import numpy as np  #pip install numpy 
import keyboard #pip install keyboard
import time     #pip install time


x = 0
flag = False
def TakePicture():
    screenshot = np.array(ImageGrab.grab(bbox=(640,220,1280,860)))
    screenshot = cv2.cvtColor(screenshot,cv2.COLOR_BGR2RGB)
    cv2.imwrite(file_name , screenshot)
    
    

while not flag:
    try:
        if keyboard.is_pressed('c'):
            
            file_name = str(x) + "_0.jpg"
            TakePicture()
            x = x + 1
            time.sleep(0.1)
        elif keyboard.is_pressed('z'):
            flag = True
    except:
        print("Game")
print('Code exits with',flag,'\nWe are eternally grateful')
