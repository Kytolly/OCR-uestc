from model.pathModel.pathToText import ImgPathToText
from app.server import server

def main():
    print("server starting...")
    server(ImgPathToText)
    
if __name__ == "__main__":
    main()