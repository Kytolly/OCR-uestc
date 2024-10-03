import time
import zmq

tcpPort = "5555"
serverHost = "tcp://*:"
coding = "utf-8"

def server(process):
    # 创建ZMQ套接字
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(serverHost + tcpPort)

    while True:
        #  等待客户端的请求
        message = socket.recv()
        print(f"Received request: {message}")

        #  Do some 'work'
        time.sleep(1)
        print("processing the message...")
        data = message.decode(coding)
        res = process(data).encode(coding)

        #  响应数据发送给客户端
        socket.send(res)
        print(f"Sent response: {res}")