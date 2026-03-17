from port_scanner import scan_ports
from dns_lookup import dns_lookup
from password_checker import check_password

def menu():
    while True:
        print("\n=== Cybersecurity Toolkit ===")
        print("1. Port Scanner")
        print("2. DNS Lookup")
        print("3. Password Strength Checker")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            scan_ports()

        elif choice == "2":
            dns_lookup()

        elif choice == "3":
            check_password()

        elif choice == "4":
            print("Exiting toolkit.")
            break

        else:
            print("Invalid option.")

menu()
