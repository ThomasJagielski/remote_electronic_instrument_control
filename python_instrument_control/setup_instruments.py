import vxi11

ip_function_generator_top = '192.168.1.100'
ip_function_generator_bottom = '192.168.1.101'

ip_source_meter_top = '192.168.1.111'
ip_source_meter_bottom = '192.168.1.110'

ON_OFF = 'OFF'

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
# SOURCE METERS
#######################################

for ip_addr in [ip_source_meter_top, ip_source_meter_bottom]:
    source_meter = vxi11.Instrument(ip_addr)

    # Use the 'ask' method to query the IDN (Identification) of the device
    model = source_meter.ask("*IDN?")
    print(f"Connected to: {model}")

    source_meter.write("smua.source.func = smua.OUTPUT_DCVOLTS")
    source_meter.write("smua.source.autorangev = smua.AUTORANGE_ON")
    
    source_meter.write("smub.source.func = smub.OUTPUT_DCVOLTS")
    source_meter.write("smub.source.autorangev = smub.AUTORANGE_ON")

    source_meter.write("smua.source.levelv = 1.8")  # Set Voltage of Channel A
    source_meter.write("smua.source.limiti = 0.1")  # Limit Current of Channel A
    source_meter.write("smub.source.levelv = 1.8")  # Set Voltage of Channel B
    source_meter.write("smub.source.limiti = 0.1")  # Limit Current of Channel B

    if ON_OFF == 'ON':
        source_meter.write("smua.source.output = smua.OUTPUT_ON")
        source_meter.write("smub.source.output = smub.OUTPUT_ON")
    else:
        source_meter.write("smua.source.output = smua.OUTPUT_OFF")
        source_meter.write("smub.source.output = smub.OUTPUT_OFF")

    # source_meter.write("display.screen = display.SMUA")
    # source_meter.write("display.smua.measure.func = display.MEASURE_DCAMPS")
    # source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")

    # source_meter.write("display.screen = display.SMUA")
    # source_meter.write("display.smua.measure.func = display.MEASURE_DCAMPS")
    # source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")


    # source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")

    # # "smua.measure.rangei = " f"{ range }"))
    # # "smua.measure.nplc = { nplc }"
    # source_meter.write("val_i=smua.measure.i()")
    # print(source_meter.ask("print(val_i)"))
    source_meter.close()
