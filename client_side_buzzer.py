import socket

_host = '192.168.225.130'
_port = 8080
print('>>> Welcome Abulala Shaikh.\n>>> Simple program to turn the lights on and off from another computer.'
      '\n>>> Developer : ABULALA SHAIKH.\n')

try:
    sock = socket.socket()
except Exception as e:
    print("Failed TCP/IP Connection", e)


def turn_on_led(host, port):

    try:
        sock.connect((host, port))
        print("Connected to : ", host)
        print(sock.recv(1024))
        while True:
            _on = input("Switch Lights on (y/n) : ")
            if _on.__eq__("yes"):
                print(">>> Turning lights on")
                sock.send('on'.encode())
            elif _on.__eq__("no"):
                print(">>> Turning Lights off.")
                sock.send('of'.encode())

    except Exception as e:
        print(e)

    finally:
        sock.close()


turn_on_led(_host, _port)
