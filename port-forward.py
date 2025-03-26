# Author: Mario Scondo (www.Linux-Support.com)
# Date: 2010-01-08
# Script template by Stephen Chappell
#
# This script forwards a number of configured local ports
# to local or remote socket servers.
#
# Configuration:
# Add to the config file port-forward.config lines with
# contents as follows:
#   <local incoming port> <dest hostname> <dest port>
#
# Start the application at command line with 'python port-forward.py'
# and stop the application by keying in <ctrl-c>.
#
# Error messages are stored in file 'error.log'.
#

import socket
import sys
import _thread
import time

def main(setup, error, args):
    # open file for error messages
    sys.stderr = open(error, 'a')

    # if args
    if (len(args) > 0):
        for settings in parse_args(args):
            _thread.start_new_thread(server, settings)
    else:
        # Display an error and exit: I've removed support for the file-based config
        sys.stderr.write('This version does not support the file-based config')
        exit(1)
    # wait for <ctrl-c>
    while True:
       time.sleep(60)

def parse_args(args):
    settings = list()
    for line in args:
        parts = line.split(":")
        settings.append((int(parts[0]), parts[1], int(parts[2])))
    return settings

def server(*settings):
    print(f'Forwarding localhost:{settings[0]} to {settings[1]}:{settings[2]}')
    try:
        dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dock_socket.bind(('', settings[0]))
        dock_socket.listen(5)
        while True:
            client_socket = dock_socket.accept()[0]
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((settings[1], settings[2]))
            _thread.start_new_thread(forward, (client_socket, server_socket))
            _thread.start_new_thread(forward, (server_socket, client_socket))
    finally:
        _thread.start_new_thread(server, settings)

def forward(source, destination):
    string = ' '
    while string:
        string = source.recv(1024)
        if string:
            destination.sendall(string)
        else:
            source.shutdown(socket.SHUT_RD)
            destination.shutdown(socket.SHUT_WR)

if __name__ == '__main__':
    main('port-forward.config', 'error.log', sys.argv[1:])