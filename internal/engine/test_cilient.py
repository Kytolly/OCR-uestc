import zmq
import setting as st
from input.input import *

cilientHost = "tcp://localhost:"
imgPath = '/home/kytolly/Project/PythonProject/OCR-uestc/internal/engine/cache/image3.png'

def TestCilient():
    context = zmq.Context()
    print("Connecting to server…")
    socket = context.socket(zmq.REQ)
    socket.connect(cilientHost+st.tcpPort)

    input_obj = Input(
        img_path=imgPath,
        statusOK=True,
        formatCode=0,
    )
    input_data = input_obj.serialize()
    
    for i in range(10):
        print(f"Sending request {i} …")
        socket.send(input_data)

        #  得到响应
        output_data = socket.recv()
        output_dic = output_data.decode(st.coding)
        print(f"Received reply {i} [ {output_dic} ]")

if __name__ == "__main__":
    TestCilient()