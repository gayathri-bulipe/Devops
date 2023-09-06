import socket
import json
import threading


def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


def send_message(server_info, message, max_buffer_size):
    try:
        server_ip = server_info['ip']
        server_port = server_info['port']

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.send(message.encode())
        if message.lower() != 'exit':
            response = client_socket.recv(max_buffer_size).decode()
            print(f"Response from {server_ip}:{server_port}: {response}")

        client_socket.close()
    except Exception as e:
        print(f"Error connecting to {server_ip}:{server_port}: {e}")


def send_broadcast_message():
    try:
        config = read_config('config_file.json')
        max_buffer_size = config['max_buffer_size']

        while True:
            message = input("Enter the broadcast message : ")
            if message.lower() == 'exit':
                send_exit_message(config, max_buffer_size)
                break

            threads = []
            for server_info in config['servers']:
                thread = threading.Thread(target=send_message, args=(server_info, message, max_buffer_size))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")


def send_exit_message(config, max_buffer_size):
    for server_info in config['servers']:
        send_message(server_info, 'exit', max_buffer_size)


if __name__ == "__main__":
    send_broadcast_message()
