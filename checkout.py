#! usr/bin/env python
import serial
from serial.serialutil import STOPBITS_ONE
from time import sleep
 
 
def send_command(ser: serial.Serial, command: str, wait_time: float = 1):
    command_to_send = command + "\r"
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    print(ser.read(ser.inWaiting()).decode('utf-8'), end="")

def login(vendor):
    with open("\\{}\\default_login.txt".format(vendor))as file:
        for line in file.readlines():
            send_command(line)

def send_command_write(ser: serial.Serial, vendor, filename, wait_time: float = 0.5):
    with open('\\{}\\checkout.txt'.format(vendor)) as commands:
        for line in commands.readlines:
            send_command(ser, line)
    sleep(wait_time)
    output=(ser.read(ser.inWaiting()).decode('utf-8'))
    with open(filename,"a+") as file:
        file.write(output)


def main():
    vendors={"1":"Juniper","2":"Cisco","3":"HPE","4":"Dell"}
    while True:
        vendor=input("Select Vendor(1-4): \n1.Juniper \n2.Cisco \n3.HPE \n4.Dell\n")
        if vendor not in vendors.keys():
            continue
        else:
            break
    file_name=input("Checkout File Name: \n") 
    with serial.Serial("COM5", timeout=1) as ser:
        print(f"Connecting to {ser.name}...")
        send_command(ser, "")
        login(vendors[vendor])
        send_command_write(ser, vendors[vendor],file_name,wait_time=2)
        send_command(ser, "exit")
        send_command(ser, "exit")
        print(f"Connection to {ser.name} closed.")


if __name__=="__main__":
    main()