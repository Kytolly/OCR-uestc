import cv2
import pytesseract 
from model.process import *

def display(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getText(image):
    # 票据类型的文字识别 
    gray = process_normal(image)
    # display(gray)
    ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) 
    text = pytesseract.image_to_string(thresh)
    # if text is not str:
    #     text = ""
    return text