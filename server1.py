import socket

class UDPServerNode:

    def __init__(self, udp_port):
        self.udp_port = udp_port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', self.udp_port))

    def run(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(72)  # buffer size is 72 bytes

                # Print received data in hexadecimal format
                print("Received Data:", ' '.join(f'{byte:02X}' for byte in data))

                # Rest of your code...
                # (including checksum verification and data processing)

            except BlockingIOError:
                pass  # No data to receive

if __name__ == '__main__':
    udp_port = 3000  # Set the desired port to listen on
    udp_server = UDPServerNode(udp_port)
    udp_server.run()
