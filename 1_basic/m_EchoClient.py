import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    """ A simple echo client"""
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server
    server_address = (host, port)
    print('Connectin to %s port %s' % server_address)
    sock.connect(server_address)

    # Send data
    try:
        #Send data
        message = b'Test message. This will be echoed'
        print('Sending %s' % message.decode())
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('Received: %s' % data.decode())
    except socket.errno as e:
        print('Socket error: %s' % e)
    except Exception as e:
        print('Other excpetion: %s' % e)
    finally:
        print('Closing connecitno to the server')
        sock.close()

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)