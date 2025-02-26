import vxi11

# https://download.tek.com/manual/2600BS-901-01_C_Aug_2016_2.pdf

# Replace with the correct IP address of your SDG 1032X
# device_ip = '192.168.1.111'
device_ip = '192.168.1.110'

# Create a connection to the instrument
inst = vxi11.Instrument(device_ip)

# Use the 'ask' method to query the IDN (Identification) of the device
model = inst.ask("*IDN?")
print(f"Connected to: {model}")

inst.write("smua.source.levelv = 3.3")  # Set Voltage of Channel A
inst.write("smua.source.limiti = 0.1")  # Limit Current of Channel A
inst.write("smub.source.levelv = 1.8")  # Set Voltage of Channel B
inst.write("smub.source.limiti = 0.1")  # Limit Current of Channel B

inst.write("smua.source.output = smua.OUTPUT_ON")
inst.write("smua.source.output = smua.OUTPUT_ON")

# inst.write("smua.source.output = smua.OUTPUT_OFF")
# inst.write("smub.source.output = smua.OUTPUT_OFF")

inst.write("smua.measure.autorangei = smua.AUTORANGE_ON")

# "smua.measure.rangei = " f"{ range }"))
# "smua.measure.nplc = { nplc }"
inst.write("val_i=smua.measure.i()")
print(inst.ask("print(val_i)"))


# inst.write("SOUR:FUNC VOLT")  # Set the source function to voltage
# inst.write("SOUR:VSET 5 ")  # Set the output voltage to 5V

# # inst.write("OUTP ON")  # Turn on the output
# inst.write("OUTP OFF")  # Turn off the output

