import vxi11
import os
import time

# https://download.tek.com/manual/3-MDO-Oscilloscope-Programmer-Manual-077149800.pdf

# Replace with the correct IP address of your SDG 1032X
device_ip = '192.168.1.102'

# Create a connection to the instrument
inst = vxi11.Instrument(device_ip)

# Use the 'ask' method to query the IDN (Identification) of the device
model = inst.ask("*IDN?")
print(f"Connected to: {model}")

# inst.write('SELECT:CH1 ON')
# inst.write('SELECT:CH2 ON')
# inst.write('SELECT:CH3 ON')
# inst.write('SELECT:CH4 ON')

inst.write('SELECT:CH1 OFF')
inst.write('SELECT:CH2 OFF')
inst.write('SELECT:CH3 ON')
inst.write('SELECT:CH4 ON')


inst.write(':AUTOSET EXECUTE')

inst.write("HORIZONTAL:SCALE 200E-6")

inst.write("CH3:SCALE 1.5")
inst.write("CH4:SCALE 1.5")

# inst.write("HORizontal:SCAle 20E-9")
time.sleep(2)

inst.write('MEASUREMENT:IMMED:SOURCE CH3')
inst.write('MEASUREMENT:IMMED:TYPE FREQUENCY')
print('Channel 3: ', inst.ask('MEASUREMENT:IMMED:VALUE?'), sep='')

inst.write('MEASUREMENT:IMMED:SOURCE CH4')
inst.write('MEASUREMENT:IMMED:TYPE FREQUENCY')
print('Channel 4: ', inst.ask('MEASUREMENT:IMMED:VALUE?'), sep='')
# print(inst.write('MEASUREMENT:IMMED?'))

inst.write("SAVe:IMAGe:INKSaver OFF")
inst.write('SAVE:IMAGE:FILEFORMAT PNG')
# inst.write("HARDcopy:IMMed:TYPe PNG")  # Set the type to PNG before capturing
inst.write("HARDcopy START")
image_data = inst.read_raw()  # Use read_raw() to get binary data

# Specify the file path where the image should be saved
file_path = 'oscilloscope_image.png'

# Write the binary image data to a file
with open(file_path, 'wb') as f:
    f.write(image_data)

print(f"Image saved to {file_path}")


# inst.ask(":DISP:SCRN:DATA?")
# inst.write(":DAT:SOU CH4")
# inst.write(":DAT:START 1")
# inst.write(":DAT:STOP 1000")

# inst.write(":WFMO:ENC BINARY")
# inst.write(":WFMO:BYT_N 1")
# inst.write(":HEAD 1")
# print(inst.write(":WFMO?"))
# print(inst.write(":CURVE?"))

