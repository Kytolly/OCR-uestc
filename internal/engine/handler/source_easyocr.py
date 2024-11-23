import easyocr 
from input.input import *
from output.output import *
from output.outputJson import *
from utils.time_str import *

class Handler_easyocr():
    def __init__(self):
        self.OCR_reader = easyocr.Reader(
            lang_list=['ch_sim', 'en'], 
            gpu=False, 
            download_enabled=True 
        )
        
    def handle(self, i: Input):
        res = self.OCR_reader.readtext(i.img_path, detail=1)
        out = Output(
                oId=now_time_string(i.hash_name()),
                statusOK=False,
                msgCode=ERROR_OUTPUT_EMPTY,
                records=[]
            )
        out.fit(res)
        return out