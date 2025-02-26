import pyvisa

# Initialize VISA resource manager
rm = pyvisa.ResourceManager()

# keithley = rm.open_resource('ASRL/dev/ttyUSB4::INSTR')
keithley = rm.open_resource('ASRL/dev/ttyUSB0::INSTR')

print(keithley.query("*IDN?"))

keithley.write('SYST:REM')
# keithley.write('*RST')

for i in range(100):
    ch1_current = keithley.query('MEAS:CURR:DC? CH1').replace('\n', '')
    ch2_current = keithley.query('MEAS:CURR:DC? CH2').replace('\n', '')
    ch3_current = keithley.query('MEAS:CURR:DC? CH3').replace('\n', '')

    ch1_power = keithley.query('MEAS:POW:DC? CH1').replace('\n', '')
    ch2_power = keithley.query('MEAS:POW:DC? CH2').replace('\n', '')
    ch3_power = keithley.query('MEAS:POW:DC? CH3').replace('\n', '')

    print("VCCA: Voltage=1.8V, Current=", ch1_current, "A, Power=", ch1_power, "W | VCCD18=1.8: Current=", ch2_current, "A, Power=", ch2_power, "W | VCCD33: Current=", ch3_current, "A, Power=", ch3_power, "W")

    # print("Channel 1: Voltage=1.8V, Current=", ch1_current, "A, Power=", ch1_power, "W", sep='')
    # print("Channel 2: Voltage=1.8V, Current=", ch2_current, "A, Power=", ch2_power, "W", sep='')
    # print("Channel 3: Voltage=3.3V, Current=", ch3_current, "A, Power=", ch3_power, "W", sep='')

# Close the connection
keithley.close()