import vxi11
import os
import time

# https://download.tek.com/manual/3-MDO-Oscilloscope-Programmer-Manual-077149800.pdf

# Replace with the correct IP address of your SDG 1032X
device_ip = '192.168.1.200'

# Create a connection to the instrument
inst = vxi11.Instrument(device_ip)

# Use the 'ask' method to query the IDN (Identification) of the device
model = inst.ask("*IDN?")
print(f"Connected to: {model}")

inst.write("*RST")
# inst.write("TIME:SCALE 2e-6")
inst.write("MEASURE:AUTOSCALE")

inst.close()