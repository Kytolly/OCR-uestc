from model.utils.process import getRatio, findContours, four_point_transform 

def filterTransform(edged, resized):
    # 透视变换的过滤器
    screenCnt = findContours(edged) 
    ratio = getRatio(resized)
    warped = four_point_transform(resized, screenCnt[0].reshape(4,2)*ratio)
    return warped