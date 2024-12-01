import easyocr
path = 'engine/image3.png'

OCR_reader = easyocr.Reader(
            lang_list=['ch_sim', 'en'], 
            gpu=False, 
            # download_enabled=True,
            model_storage_directory= 'D:/Desktop/myfile/UESTC-courses/Grade5/软件工程/OCR-uestc/internal/engine/model'
        )

result = OCR_reader.readtext(path, detail=1)
