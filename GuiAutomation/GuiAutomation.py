from turtle import Screen
from PIL import Image
from numpy import asarray
import numpy as np
import pyautogui
import re
import cv2
import os
import time

#variables with file paths to images
MainPath = os.path.dirname(str(__file__))+"\\Img\\"


def Screenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(MainPath+"/desktop.png", image)    

def CheckSubpic(subimgpath):
    img = cv2.imread(MainPath+"/desktop.png")              #main image
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    template = cv2.imread(subimgpath, cv2.IMREAD_GRAYSCALE)      #subimage
    w,h = template.shape[::-1]

    result = cv2.matchTemplate(gray_img,template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)

    x = ((template.shape[1])/2)-10
    y = ((template.shape[0])/2)+10
   
    return loc,x,y


def ClickCenter(MainArray, Xo, Yo,file_path):
    # Calculate the average position of the image in the screenshot
    Avg_x = int(sum(MainArray[1])/3)
    Avg_y = int(sum(MainArray[0])/3)

    # Open the image and calculate its center
    image = Image.open(file_path)
    data = asarray(image)
    array = data.shape
    Centerx = Avg_x + int(array[1]/2)
    Centery = Avg_y + int(array[0]/2)

    # Click on the center of the image
    pyautogui.doubleClick(Centerx,Centery, interval=0.25)



def DesktopView():
    pyautogui.keyDown('win')
    pyautogui.press('d')
    pyautogui.keyUp("win")



if __name__ == "__main__":
    
    #go to main view
    DesktopView()

    time.sleep(1)

    Screenshot()

    location, x, y = CheckSubpic(MainPath+"/notepad.png")

    ClickCenter(location,x,y,MainPath+"/notepad.png")
    