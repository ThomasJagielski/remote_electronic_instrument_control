# sudo ip route add 192.168.1.0/24 dev enp0s31f6
# ip route show

# https://siglentna.com/USA_website_2014/Documents/Program_Material/SDG_ProgrammingGuide_PG_E03B.pdf


import vxi11

# Replace with the correct IP address of your SDG 1032X
device_ip = '192.168.1.101'

# Create a connection to the instrument
inst = vxi11.Instrument(device_ip)

# Use the 'ask' method to query the IDN (Identification) of the device
model = inst.ask("*IDN?")
print(f"Connected to: {model}")


# inst.write("C1:BSWV WVTP,SQUARE")

inst.write("C1:BSWV WVTP,SINE")
inst.write("C1:BSWV FRQ,25000000")
inst.write("C1:BSWV AMP,0.4")
inst.write("C1:BSWV OFST,1")
inst.write("C1:BSWV PHSE,0")

inst.write("C2:BSWV WVTP,SINE")
inst.write("C2:BSWV FRQ,25000000")
inst.write("C2:BSWV AMP,0.4")
inst.write("C2:BSWV OFST,1")
inst.write("C2:BSWV PHSE,180")

# inst.write("C1:OUTP ON")
# inst.write("C2:OUTP ON")

inst.write("C1:OUTP OFF")
inst.write("C2:OUTP OFF")

# print(inst.write("C2:OUTP OFF"))

# Example: Set the frequency of channel 1 to 1 kHz
# inst.write("SOUR1:FREQ 1000")

# # Query the frequency value of channel 1
# frequency = inst.ask("SOUR1:FREQ?")
# print(f"Channel 1 Frequency: {frequency}")

# Close the connection
inst.close()
