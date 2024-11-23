import time
import zmq
import setting as st 
from filter.gray import *
from filter.edge import *
from filter.transform import * 
from handler.source_easyocr import *
from input.input import *


def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(st.serverHost + st.tcpPort)
    while True:
        input_data = socket.recv()
        input_obj = Input.deserialize(input_data)
        
        output_obj = Handler_easyocr().handle(input_obj)

        output_data = output_obj.serialize()
        socket.send(output_data)
        