#! usr/bin/env python
import serial
from serial.serialutil import STOPBITS_ONE

import serial
from time import sleep
 
 
def send_to_console(ser: serial.Serial, command: str, wait_time: float = 0.5):
    command_to_send = command + "\r"
    ser.write(command_to_send.encode('utf-8'))
    sleep(wait_time)
    print(ser.read(ser.inWaiting()).decode('utf-8'), end="")
 
with serial.Serial("COM5", timeout=1) as ser:
    print(f"Connecting to {ser.name}...")
    send_to_console(ser, "")
    send_to_console(ser, "username")
    send_to_console(ser, "pw")
    send_to_console(ser, "cli")
    send_to_console(ser, "show version", wait_time=2)
    send_to_console(ser, "show chassis hardware", wait_time=2)
    send_to_console(ser, "show chassis environment", wait_time=2)
    send_to_console(ser, "show chassis fpc")
    send_to_console(ser, "show chassis fpc pic-status")
    print(f"Connection to {ser.name} closed.")