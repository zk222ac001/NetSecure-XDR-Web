import socket

common_ports = [21, 22, 80, 443, 3389]

def scan_target(host):

    results = []

    for port in common_ports:

        sock = socket.socket()

        sock.settimeout(1)

        result = sock.connect_ex((host, port))

        if result == 0:

            results.append(port)

        sock.close()

    return results