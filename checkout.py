#! usr/bin/env python
import serial, sys
from serial.serialutil import STOPBITS_ONE
from time import sleep
 
 
def send_command(ser: serial.Serial, command: str, wait_time: float = 1):
    command_to_send = command + "\r"
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    print(ser.read(ser.inWaiting()).decode('utf-8'), end="")

def login(vendor):
    with open("\\{}\\default_login.txt")as file:
        for line in file.readlines():
            send_command(line)

def send_command_write(ser: serial.Serial, vendor, wait_time: float = 0.5, filename=sys.argv(2), ):
    with open(filename) as commands:
        for line in commands.readlines:
            send_command(ser, line)
    sleep(wait_time)
    output=(ser.read(ser.inWaiting()).decode('utf-8'))
    with open(filename,"a+") as file:
        file.write(output)


def main():
    vendors={"1":"Juniper","2":"Cisco","3":"HPE","4":"Dell"}
    vendor=input("Select Vendor(1-4): \b1.Juniper \b2.Cisco \b3.HPE \b4.Dell\b")

    file_name=input("Checkout File Name: \b") 
    with serial.Serial("COM5", timeout=1) as ser:
        print(f"Connecting to {ser.name}...")
        send_command(ser, "")
        login(vendors[vendor])
        send_command_write(ser, vendors[vendor],wait_time=2)
        send_command(ser, "exit")
        send_command(ser, "exit")
        print(f"Connection to {ser.name} closed.")


if __name__=="__main__":
    main()