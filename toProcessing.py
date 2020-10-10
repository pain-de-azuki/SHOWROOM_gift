

import socket

host = "127.0.0.1" #Processingで立ち上げたサーバのIPアドレス
port = 10001       #Processingで設定したポート番号

if __name__ == '__main__':
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成
    socket_client.connect((host, port))                               #サーバに接続

    #socket_client.send('送信するメッセージ')                #データを送信 Python2
    socket_client.send('hello world'.encode('utf-8')) #データを送信 Python3
