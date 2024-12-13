import easyocr 
from input.input import *
from output.output import *
from output.outputJson import *
from utils.time_str import *
from pdf2image import convert_from_path
import requests
import tempfile
import shutil
from urllib.parse import urlparse
import os

def getDirofThisExcutable():
    return os.getcwd()

class Handler_easyocr():
    def __init__(self):
        self.OCR_reader = easyocr.Reader(
            lang_list=['ch_sim', 'en'], 
            gpu=False, 
            download_enabled=True,
            model_storage_directory= '../model'
        )
    
    def handle(self, i: Input):
        paths = self.getImagePaths(i)
        results = []
        for p in paths:
            p = os.path.join(getDirofThisExcutable(), p)
            result = self.OCR_reader.readtext(p, detail=1)
            for r in result:
                results.append(r)
        out = Output(
                oId=now_time_string(i.hash_name()),
                statusOK=False,
                msgCode=ERROR_OUTPUT_EMPTY,
                records=[]
            )
        out.fit(results)
        return out
    
p = "cache/test.png"
h = Handler_easyocr()
result = h.OCR_reader.readtext(p, detail=1)
print(result)
