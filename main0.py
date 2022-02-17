import time
import socket
import ssl
import time
from network import LTE
from machine import RTC
from machine import UART



lte = LTE()         # instantiate the LTE object
lte.attach()        # attach the cellular modem to a base station
print("no to jazda")
while not lte.isattached():
    time.sleep(0.25)

print("no to jest")
lte.connect()       # start a data session and obtain an IP address
while not lte.isconnected():
    time.sleep(1)

s = socket.socket()
s = ssl.wrap_socket(s)
s.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
s.send(b"GET / HTTP/1.0\r\n\r\n")
print(s.recv(4096))
s.close()

lte.disconnect()
lte.dettach()



rtc = RTC()
rtc.init((2014, 5, 1, 4, 13, 0, 0, 0))
print(rtc.now())





uart = UART(1, 115200)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters
