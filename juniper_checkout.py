#! usr/bin/env python
import serial, sys
from serial.serialutil import STOPBITS_ONE
from time import sleep
 
 
def send_to_console(ser: serial.Serial, command: str, wait_time: float = 0.5):
    command_to_send = command + "\r"
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    print(ser.read(ser.inWaiting()).decode('utf-8'), end="")

def send_to_console_write(ser: serial.Serial, vendor=sys.argv(1), wait_time: float = 0.5, filename=sys.argv(2), ):
    with open(filename) as commands:
        for line in commands.readlines:
            send_to_console(ser, line)
    sleep(wait_time)
    output=(ser.read(ser.inWaiting()).decode('utf-8'))
    with open(filename,"a+") as file:
        file.write(output)


def main(): 
    with serial.Serial("COM5", timeout=1) as ser:
        print(f"Connecting to {ser.name}...")
        send_to_console(ser, "")
        send_to_console(ser, "username")
        send_to_console(ser, "pw")
        send_to_console(ser, "cli")
        send_to_console_write(ser, "show version", wait_time=2)
        send_to_console(ser, "exit")
        send_to_console(ser, "exit")
        print(f"Connection to {ser.name} closed.")


if __name__=="__main__":
    main()