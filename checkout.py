#! usr/bin/env python
import serial
import serial.tools.list_ports
from serial.serialutil import STOPBITS_ONE, SerialBase, SerialException
from time import sleep
 
 
def send_command(ser: serial.Serial, command: str, wait_time: float = 3):
    command_to_send = command + "\r"
    print(".")
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    #print(ser.read(ser.inWaiting()).decode('utf-8'), end="")

def login(ser: serial.Serial,vendor):
    with open("{}\\default_login.txt".format(vendor),"r")as file:
        for line in file:
            send_command(ser,line)
            sleep(1)
            output=(ser.read(ser.inWaiting()).decode('utf-8'))
            
    

def send_command_write(ser: serial.Serial, vendor, filename, wait_time: float = 3):
    with open('{}\\checkout.txt'.format(vendor),"r") as commands:
        for line in commands:
            send_command(ser, line)
            sleep(wait_time)
            output=(ser.read(ser.inWaiting()).decode('utf-8'))
            with open(filename,"a") as file:
                file.write(output)

def show_serial_ports():
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {}".format(port, desc))
    
def main():
    vendors={"1":"Juniper","2":"Cisco","3":"HPE","4":"Dell"}
    baud_rates={"Juniper":9600,"Cisco":9600,"HPE":115100, "Dell":9600}
    while True:
        vendor=input("Select Vendor(1-4): \n1.Juniper \n2.Cisco \n3.HPE \n4.Dell\n")
        if vendor not in vendors.keys():
            continue
        else:
            break
    baudrate=baud_rates[vendors[vendor]]
    while True:
        available_coms=show_serial_ports()
        com=input("\nSelect COM port number: \n")
        if com.isnumeric():
            break
        else:
            continue
    file_name=input("Checkout File Name: \n")+".txt" 
    try:


        with serial.Serial("COM"+com,baudrate,timeout=2 ) as ser:
            print(f"Connecting to {ser.name}...")
            send_command(ser, command=" ")
            send_command(ser, command=" ")
            send_command(ser, command=" ")
            send_command(ser, command=" ")
            login(ser, vendors[vendor])
            send_command_write(ser, vendors[vendor],file_name,wait_time=5)
            send_command(ser, "exit")
            send_command(ser, "exit")
            print(f"Session complete! \nConnection to {ser.name} closed.")
    except SerialException:
        print("Unable to reach device. Please select a connected device.")
    except ValueError:
        print("Incorrect parameters. Unable to connect.")



if __name__=="__main__":
    main()