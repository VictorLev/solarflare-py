import network
import machine
import config
from time import sleep
from machine import Pin
import socket
import os

# Configure the LED pin
led = Pin(2, Pin.OUT)

# Connect to Wi-Fi
ssid = config.SSID
password = config.PASSWORD

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    sleep(1)

print('Connected to Wi-Fi')

# Create a socket and listen for connections
addr = socket.getaddrinfo('192.168.20.12', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)

def read_html(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Serve a simple web page
while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    request = str(request)

    # Check the path in the request and toggle the LED accordingly
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')

    if led_on == 6:
        print('LED ON')
        led.value(1)
    if led_off == 6:
        print('LED OFF')
        led.value(0)

    # Send a simple HTML response
    response = read_html('index.html')
    cl.send(response)
    cl.close()
