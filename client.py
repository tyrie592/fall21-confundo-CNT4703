#!/usr/bin/env python3

import argparse
import os
import socket
import sys

import confundo

parser = argparse.ArgumentParser("Parser")
parser.add_argument("host", help="Set Hostname")
parser.add_argument("port", help="Set Port Number", type=int)
parser.add_argument("file", help="Set File Directory")
args = parser.parse_args()

def start():
    try:
        with confundo.Socket() as s:
            sock.settimeout(10)
            sock.connect((host, port))

            response = b''
            while response[-2:] != b'\r\n':
                got = sock.recv(1)
                response += got

            if response == b'accio\r\n':
                with open(filename, "rb") as f:
                    data = f.read(1024)
                    while data:
                        total_sent = 0
                        while total_sent < len(data):
                            sent = sock.send(data[total_sent:])
                            total_sent += sent
                            data = f.read(1024)
    except RuntimeError as e:
        sys.stderr.write(f"ERROR: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    start()
