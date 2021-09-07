#! usr/bin/env python
import serial, sys
from serial.serialutil import STOPBITS_ONE
from time import sleep
 
 
def send_command(ser: serial.Serial, command: str, wait_time: float = 0.5):
    command_to_send = command + "\r"
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    print(ser.read(ser.inWaiting()).decode('utf-8'), end="")

def send_command_write(ser: serial.Serial, vendor=sys.argv(1), wait_time: float = 0.5, filename=sys.argv(2), ):
    with open(filename) as commands:
        for line in commands.readlines:
            send_command(ser, line)
    sleep(wait_time)
    output=(ser.read(ser.inWaiting()).decode('utf-8'))
    with open(filename,"a+") as file:
        file.write(output)


def main(): 
    with serial.Serial("COM5", timeout=1) as ser:
        print(f"Connecting to {ser.name}...")
        send_command(ser, "")
        send_command(ser, "username")
        send_command(ser, "pw")
        send_command(ser, "cli")
        send_command_write(ser, wait_time=2)
        send_command(ser, "exit")
        send_command(ser, "exit")
        print(f"Connection to {ser.name} closed.")


if __name__=="__main__":
    main()