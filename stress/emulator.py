import socket
import threading

import create_messages

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 7002))
server_socket.listen(5)

cm = create_messages.create_messages()
list_of_input_byte_array = list()
for i in range(0, 10000):
    input_list_parser, input_byte_array = cm.create_TRACK_EXTENDED_message(100)
    list_of_input_byte_array.append(input_byte_array)


def sending_messages():
    while True:
        connection, address = server_socket.accept()
        print(address)
        for k in range(0, 10000):
            connection.sendall(list_of_input_byte_array[k])
            print("just sent message number:", k)
        break


def run_with_threading():
    for j in range(15):
        thread = threading.Thread(target=sending_messages)
        thread.start()


def run_with_no_threading():
    sending_messages()

def with_10000_trackID():
    pass


def main():
    run_with_threading()
    # run_with_no_threading()


if __name__ == "__main__":
    main()
