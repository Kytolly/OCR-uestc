import numpy as np
import cv2
from setting.load import coding

def inputToImg(message: bytes):
    path = message.decode(coding)
    img = cv2.imread(path)
    return img