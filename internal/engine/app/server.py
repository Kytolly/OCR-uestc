import time
import zmq
from setting.load import serverHost, tcpPort, coding
from model.getImg import inputToImg 
from model.getText import getText

def server():
    # 创建ZMQ套接字
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(serverHost + tcpPort)

    while True:
        #  等待客户端的请求
        message = socket.recv()
        # print(f"Received request: {message}")

        #  Do some 'work'
        # time.sleep(1)
        # print("processing the message...")
        img = inputToImg(message)
        text = getText(img)
        res = text.encode(coding)

        #  响应数据发送给客户端
        socket.send(res)
        # print(f"Sent response: {res}")