import zmq
from server import tcpPort, coding

cilientHost = "tcp://localhost:"
imgPath = '/home/kytolly/Project/PythonProject/OCR-uestc/internal/ocrModule/data/image1.png'

def TestCilient():
    context = zmq.Context()
    #  客户端连接至服务端
    print("Connecting to server…")
    socket = context.socket(zmq.REQ)
    socket.connect(cilientHost+tcpPort)

    #  测试10个请求
    data = bytes(imgPath, coding)
    for request in range(10):
        print(f"Sending request {request} …")
        socket.send(data)

        #  得到响应
        message = socket.recv()
        res = message.decode(coding)
        print(f"Received reply {request} [ {res} ]")

if __name__ == "__main__":
    TestCilient()