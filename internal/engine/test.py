import cv2
from model.process import *
from model.getText import *

def test():
    image = cv2.imread('data/image4.png')
    text = getText(image)
    print(text)
    
if __name__ == '__main__':
    test()