import socket

def dns_lookup():
    domain = input("Enter domain: ")

    try:
        ip = socket.gethostbyname(domain)
        print("IP Address:", ip)

    except:
        print("Could not resolve domain.")
