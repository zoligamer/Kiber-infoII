'''
Created on 2025. márc. 13.

@author: adylaszlo
'''
import logging
from network import TCPServer, EchoConnectionHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)


def main():
    server = TCPServer("localhost", 50001, EchoConnectionHandler)
    try:
        server.start()
    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        server.close()


if __name__ == '__main__':
    main()
