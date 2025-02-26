import vxi11
import pyvisa

ON_OFF = 'OFF'

rm = pyvisa.ResourceManager()

ip_function_generator_top = '192.168.1.100'
ip_function_generator_bottom = '192.168.1.101'

ip_source_meter_top = '192.168.1.111'
ip_source_meter_bottom = '192.168.1.110'

power_supply_top = 'ASRL/dev/ttyUSB4::INSTR'
power_supply_bottom = 'ASRL/dev/ttyUSB0::INSTR'

#######################################
# FUNCTION GENERATORS
#######################################

for ip_addr in [ip_function_generator_top, ip_function_generator_bottom]:
    func_gen = vxi11.Instrument(ip_addr)

    model = func_gen.ask("*IDN?")
    print(f"Connected to: {model}")

    func_gen.write("C1:BSWV WVTP,SINE")
    func_gen.write("C1:BSWV FRQ,25000000")
    func_gen.write("C1:BSWV AMP,0.4")
    func_gen.write("C1:BSWV OFST,1")
    func_gen.write("C1:BSWV PHSE,0")

    func_gen.write("C2:BSWV WVTP,SINE")
    func_gen.write("C2:BSWV FRQ,25000000")
    func_gen.write("C2:BSWV AMP,0.4")
    func_gen.write("C2:BSWV OFST,1")
    func_gen.write("C2:BSWV PHSE,180")

    if ON_OFF == 'ON':
        func_gen.write("C1:OUTP ON")
        func_gen.write("C2:OUTP ON")
    else:
        func_gen.write("C1:OUTP OFF")
        func_gen.write("C2:OUTP OFF")

    func_gen.close()

#######################################
# POWER SUPPLIES
#######################################
for supply_str in [power_supply_top, power_supply_bottom]:
    keithley = rm.open_resource(supply_str)
    print(keithley.query("*IDN?"))
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
    
    keithley.close()



#######################################
# SOURCE METERS
#######################################

# for ip_addr in [ip_source_meter_top, ip_source_meter_bottom]:
#     source_meter = vxi11.Instrument(ip_addr)

#     # Use the 'ask' method to query the IDN (Identification) of the device
#     model = source_meter.ask("*IDN?")
#     print(f"Connected to: {model}")

#     source_meter.write("smua.source.func = smua.OUTPUT_DCVOLTS")
#     source_meter.write("smua.source.autorangev = smua.AUTORANGE_ON")
    
#     source_meter.write("smub.source.func = smub.OUTPUT_DCVOLTS")
#     source_meter.write("smub.source.autorangev = smub.AUTORANGE_ON")

#     source_meter.write("smua.source.levelv = 1.8")  # Set Voltage of Channel A
#     source_meter.write("smua.source.limiti = 0.1")  # Limit Current of Channel A
#     source_meter.write("smub.source.levelv = 1.8")  # Set Voltage of Channel B
#     source_meter.write("smub.source.limiti = 0.1")  # Limit Current of Channel B

#     if ON_OFF == 'ON':
#         source_meter.write("smua.source.output = smua.OUTPUT_ON")
#         source_meter.write("smub.source.output = smub.OUTPUT_ON")
#     else:
#         source_meter.write("smua.source.output = smua.OUTPUT_OFF")
#         source_meter.write("smub.source.output = smub.OUTPUT_OFF")

#     # source_meter.write("display.screen = display.SMUA")
#     # source_meter.write("display.smua.measure.func = display.MEASURE_DCAMPS")
#     # source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")

#     # source_meter.write("display.screen = display.SMUA")
#     # source_meter.write("display.smua.measure.func = display.MEASURE_DCAMPS")
#     # source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")


#     # source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")

#     # # "smua.measure.rangei = " f"{ range }"))
#     # # "smua.measure.nplc = { nplc }"
#     # source_meter.write("val_i=smua.measure.i()")
#     # print(source_meter.ask("print(val_i)"))
#     source_meter.close()
