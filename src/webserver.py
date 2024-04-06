# Description: A simple web server that toggles an LED on and off

###############################IMPORTS##########################################
# MiroPy imports
from time import sleep
import os
import socket
import network # type: ignore
from machine import Pin # type: ignore
from esp32 import raw_temperature # type: ignore

# Project imports
import config
################################################################################

# Convert the raw temperature to Celsius. Note: This conversion might not be accurate.
def read_temperature():
    temp_f = raw_temperature()
    temp_c = (temp_f - 32) / 1.8
    return temp_c

def setup():
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
    ip_address = network.WLAN(network.STA_IF).ifconfig()[0]
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)

    print('Listening on', ip_address)

    return s

def read_html(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def update_html():
    # Parse the request here and change the LED state as needed
    led = Pin(2, Pin.OUT)

    # Get the LED state
    led_state = led.value()
    temperature = read_temperature()
    statvfs = os.statvfs('/')
    ffree = statvfs[0] * statvfs[3]

    ip_address = network.WLAN(network.STA_IF).ifconfig()[0]
    mask_address = network.WLAN(network.STA_IF).ifconfig()[1]
    gateway_ip = network.WLAN(network.STA_IF).ifconfig()[2]

    # Generate the HTML content based on the LED state
    html_content = read_html('index.html')
    html_content = html_content.replace('DEVICE_TEMP', "{:.2f}".format(temperature))
    html_content = html_content.replace('DEVICE_MEM', "{:.2f} KB".format(ffree / 1024))

    html_content = html_content.replace('DEVICE_IP', ip_address)
    html_content = html_content.replace('DEVICE_MASK', mask_address)
    html_content = html_content.replace('GATEWAY_IP', gateway_ip)


    html_content = html_content.replace('LED_STATE', 'ON' if led_state == 1 else 'OFF')
    return html_content
