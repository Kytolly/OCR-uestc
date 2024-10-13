from model.utils.process import resize, getRatio, findContours, four_point_transform 
from model.filter.edge import *
from model.filter.transform import * 
from model.filter.gray import *
from setting.load import stdHeight

def process_normal(image):
    resized = resize(image, height=stdHeight)
    gray = filterGray(resized)
    return gray

def process_fourPoints(image):
    resized = resize(image, height=stdHeight)
    edged = filterEdgeDetection(resized)
    warped = filterTransform(edged, resized)
    gray = filterGray(warped)
    return gray