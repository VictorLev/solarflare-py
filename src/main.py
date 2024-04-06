# Description: A simple web server that toggles an LED on and off

###############################IMPORTS##########################################
# MiroPy imports
import machine # type: ignore
from machine import Pin # type: ignore

# Project imports
import webserver
################################################################################

# Configure the LED pin
led = Pin(2, Pin.OUT)

s = webserver.setup()

# Serve a simple web page
while True:
    cl, addr = s.accept()
    request = cl.recv(1024)
    request = str(request)

    # Check the path in the request and toggle the LED accordingly
    print(request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')

    if led_on == 6:
        print('LED ON from:', addr)
        led.value(1)
    if led_off == 6:
        print('LED OFF from:', addr)
        led.value(0)

    # Send a simple HTML response
    response = webserver.update_html()
    cl.send(response)
    cl.close()
