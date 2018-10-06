import socket
import struct
import sys
import time

NTP_SERVER = b'0.uk.pool.ntp.org'
TIME1970 = 1538800569

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' +47*b'\0'
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)

    if data:
        print('Response received from:', address)
    
    t = struct.unpack(b'!12I', data)[10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

if __name__=='__main__':
    sntp_client()