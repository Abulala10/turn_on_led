import socket
import RPi.GPIO as gpio 
from time import sleep

print('>>> Welcome Abulala Shaikh.\n>>> Simple program to turn the lights on and off from another computer.'
	  '\n>>> Developer : ABULALA SHAIKH.\n')

try:
	gpio.setwarnings(False)
	gpio.setmode(gpio.BCM)  
	LED_PIN = 27  # Pin Number 27 on Raspberry pi.
	gpio.setup(LED_PIN, gpio.OUT)
except Exception as e:
	print('General purpose input output error : ', e)


try:
	sock = socket.socket()  # Tcp/Ip connection.
	host = ''
	port = 8080
except Exception as e:
	print('Failed Tcp/Ip Connection.', e)


def connection(host, port):
	print('Waiting For Connection.........\n')
	try:
		sock.bind((host, port))
		sock.listen(5)  # listens to 5 connections
		conn, addr = sock.accept()
		print('Got Connection from : ', addr)
		conn.send('Turn on the lights for me :)')
		while True:
			if conn.recv(1024) in ('on', 'ON', 'On'):  # receiving signals from Client.
				gpio.output(LED_PIN, gpio.HIGH)
				print('>>> Lights are ON')
			elif conn.recv(1024) in ('of', 'OF', 'off', 'OFF', 'Of', 'Off'):
				gpio.output(LED_PIN, gpio.LOW)
				print('>>> Lights are OF')
	
	except Exception as e:
		print(e)
	
	finally:
		sock.close()


connection(host, port)

