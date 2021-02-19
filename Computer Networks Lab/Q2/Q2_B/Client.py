import socket 
import sys 
import argparse 
 
host = 'localhost' 
data_payload = 2048 
 
def echo_client(port): 
    """ A simple echo client """ 
    # Create a UDP socket 
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    server_address = (host, port) 
    print ("Connecting to {} port {}".format(server_address,port))
    message = 'This is the message.  It will be repeated.' 
 
    try: 
 
        # Send data 
        message = input("ENTER THE MESSAGE :") 
        print ("Sending {}".format(message)) 
        sent = sock.sendto(message.encode('utf-8'), server_address) 
 
        # Receive response 
        data, server = sock.recvfrom(data_payload) 
        print ("received {}".format(data)) 
 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 
 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Socket Server Example') 
    parser.add_argument('--port', action="store", dest="port", type=int, required=True) 
    given_args = parser.parse_args()  
    port = given_args.port 
    echo_client(port)