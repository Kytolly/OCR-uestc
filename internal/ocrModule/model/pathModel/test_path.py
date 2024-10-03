from pathToText import ImgPathToText

if __name__ == '__main__':
    imgPath = '/home/kytolly/Project/PythonProject/OCR-uestc/internal/ocrModule/data/image3.png'
    textResult = ImgPathToText(imgPath)
    print(textResult)