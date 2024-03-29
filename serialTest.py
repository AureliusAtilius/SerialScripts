import serial

#serial is the main module used and needs to be installed

import time

'''
I have a cisco 2960-s series switch hooked up to a laptop through a serial port so think of 'ser' as 'switch'
'''

#creating your serial object
ser = serial.Serial(
    port = 'COM5', #COM is on windows, linux is different
    baudrate=115100, #many different baudrates are available
    parity='N',    #no idea
    stopbits=1,
    bytesize=8,
    timeout=8      #8 seconds seems to be a good timeout, may need to be increased
    )



#open your serial object
ser.isOpen()

#in this case it returns str COM3
print(ser.name)
 
#first command (hitting enter)
command = '\r\n'

#convert str to binary (commands sent to switch must be binary)
command = str.encode(command)

#send the command to the switch
ser.write(command)

#wait a sec
time.sleep(1.5)
ser.inWaiting()

#get the response from the switch
input_data = ser.read(225) #(how many bytes to limit to read)

#convert binary to str
input_data = input_data.decode("utf-8", "ignore")

#print response


#create a loop
while 1:
    #enter your own command
    command = input(':: ') 

    #type 'exit' to end serial session with the switch
    if command == 'exit':
        ser.close()
        exit()
    
    else:
        #convert command to binary
        command = str.encode(command + '\r\n')
        
        #send command
        ser.write(command)
        
        #set response variable (empty binary str)
        out = b''
        
        #take a short nap
        time.sleep(.5)

        #while response is happening (timeout hasnt expired)
        while ser.inWaiting() > 0:
            
            #trying to read one line at a time (100 bytes at a time)
            out = ser.readline(100)
            
            #converting response to str
            out = out.decode("utf-8", "ignore")
            
            #printing response if not empty
            if out != '':
                with open("test.txt", "a") as file:
                    file.write(out)
                
            #repeat until timeout




