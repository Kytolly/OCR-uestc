import setting as st
import json
import cv2

class Input():
    def __init__(self, img_path=st.img_dir_local, statusOK=False, formatCode=0):
        self.img_path = img_path
        self.statusOK = statusOK
        self.formatCode = formatCode
        
    def __dict__(self):
        return {
            'img_path':self.img_path,
            "statusOK": self.statusOK,
            'formatCode': self.formatCode, 
        }
    
    def _json(self):
        return json.dumps(self.__dict__())
    
    def serialize(self):
        return self._json().encode(st.coding)
    
    @staticmethod
    def deserialize(data:bytes):
        sdata = data.decode(st.coding)
        dic = json.loads(sdata)
        return Input(
            img_path=dic['img_path'],
            statusOK=dic['statusOK'],  
            formatCode=dic['formatCode'], 
        )
        
    def img_data(self): 
        img = cv2.imread(self.img_path)
        return img
    
    def hash_name(self):
        return hash(self._json())