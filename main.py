#!/usr/bin/env python3

import subprocess

def main():
    while True:
        print("1. List USB devices")
        print("2. List network devices")
        print("3. Change wireless adapter mode")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_usb_devices()
        elif choice == "2":
            list_network_devices()
        elif choice == "3":
            change_wireless_mode()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def list_usb_devices():
    subprocess.run(["lsusb"])

def list_network_devices():
    subprocess.run(["iwconfig"])
    #    subprocess.run(["ip", "link"])
def change_wireless_mode():
    device = input("Enter wireless device name: ")
    mode = input("Enter mode (managed or monitor): ")
    subprocess.run(["sudo", "ip", "link", "set", device, "down"])
    subprocess.run(["sudo", "iwconfig", device, "mode", mode])
    subprocess.run(["sudo", "ip", "link", "set", device, "up"])

if __name__ == "__main__":
    main()
