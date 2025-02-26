# Example: https://github.com/tektronix/Keithley_2231A_Examples/blob/master/PyVISA_Examples/Keithley_2231A_PyVISA_Examples.py
# Reference Manual: https://download.tek.com/manual/077100401_Reference%20manual.pdf

import pyvisa

ON_OFF = 'OFF'

# Initialize VISA resource manager
rm = pyvisa.ResourceManager()

# Connect to the Keithley 2231A-30-3 via USB
# Replace 'USB0::0x05E6::0x2231::xxxxx::INSTR' with your actual VISA address
keithley = rm.open_resource('ASRL/dev/ttyUSB4::INSTR')
# keithley = rm.open_resource('ASRL/dev/ttyUSB0::INSTR')

# Query the device for its ID to confirm connection
# print(keithley.query("*IDN?"))
response = keithley.query("*IDN?")  # Query the ID
# response = response.decode("utf-8")  # Manually decode the byte response to a string

print(response)

keithley.write('SYST:REM')
# keithley.write('*RST')

keithley.write("SOURCE:APPLY CH1,1.8")  # Set voltage to 1.8V on channel 1
keithley.write("SOURCE:APPLY CH2,1.8")  # Set voltage to 1.8V on channel 1
keithley.write("SOURCE:APPLY CH3,3.3")  # Set voltage to 1.8V on channel 1

# Turn on/off the output
if ON_OFF == "ON":
    keithley.write("OUTP 1")
else:
    keithley.write("OUTP 0")

ch1_current = keithley.query('MEAS:CURR:DC? CH1').replace('\n', '')
ch2_current = keithley.query('MEAS:CURR:DC? CH2').replace('\n', '')
ch3_current = keithley.query('MEAS:CURR:DC? CH3').replace('\n', '')

ch1_power = keithley.query('MEAS:POW:DC? CH1').replace('\n', '')
ch2_power = keithley.query('MEAS:POW:DC? CH2').replace('\n', '')
ch3_power = keithley.query('MEAS:POW:DC? CH3').replace('\n', '')

print("Channel 1: Voltage=1.8V, Current=", ch1_current, "A, Power=", ch1_power, "W", sep='')
print("Channel 2: Voltage=1.8V, Current=", ch2_current, "A, Power=", ch2_power, "W", sep='')
print("Channel 3: Voltage=3.3V, Current=", ch3_current, "A, Power=", ch3_power, "W", sep='')


# Close the connection
keithley.close()


# import pyvisa

# # Initialize the VISA resource manager
# rm = pyvisa.ResourceManager()

# # List all connected VISA resources (including USB instruments)
# resources = rm.list_resources()

# # Print the list of resources
# print("Connected VISA Resources:")
# for resource in resources:
#     print(resource)
