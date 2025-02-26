import vxi11

# https://download.tek.com/manual/2600BS-901-01_C_Aug_2016_2.pdf

ip_source_meter_top = '192.168.1.111'
ip_source_meter_bottom = '192.168.1.110'

mapping_dict = {
    "top_a": "BOARD1_VCCA",
    "top_b": "BOARD2_???????",
    "bottom_a": "BOARD1_VCCD18",
    "bottom_b": "BOARD2_?????"
}

# print(mapping_dict)

#######################################
# TOP SOURCE METER
#######################################
for i in range(100):
    top_source_meter = vxi11.Instrument(ip_source_meter_top)
    # Channel A
    top_source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")
    top_source_meter.write("smua.measure.autorangev = smua.AUTORANGE_ON")
    top_source_meter.write("val_ia, val_va=smua.measure.iv()")
    top_source_meter.write("val_pa=smua.measure.p()")
    top_current_a = top_source_meter.ask("print(val_ia)")
    top_voltage_a = top_source_meter.ask("print(val_va)")
    top_power_a = top_source_meter.ask("print(val_pa)")
    print(mapping_dict["top_a"], ": top_a_power=", top_power_a, ", top_a_current=", top_current_a, ", top_a_voltage=", top_voltage_a, sep='')

    # Channel B
    top_source_meter.write("smub.measure.autorangei = smub.AUTORANGE_ON")
    top_source_meter.write("smub.measure.autorangev = smub.AUTORANGE_ON")
    top_source_meter.write("val_ib, val_vb=smub.measure.iv()")
    top_source_meter.write("val_pb=smub.measure.p()")
    top_current_b = top_source_meter.ask("print(val_ib)")
    top_voltage_b = top_source_meter.ask("print(val_vb)")
    top_power_b = top_source_meter.ask("print(val_pb)")
    print(mapping_dict["top_b"], ": top_b_power=", top_power_b, ", top_b_current=", top_current_b, ", top_b_voltage=", top_voltage_b, sep='')

    #######################################
    # BOTTOM SOURCE METER
    #######################################
    bottom_source_meter = vxi11.Instrument(ip_source_meter_bottom)
    # Channel A
    bottom_source_meter.write("smua.measure.autorangei = smua.AUTORANGE_ON")
    bottom_source_meter.write("smua.measure.autorangev = smua.AUTORANGE_ON")
    bottom_source_meter.write("val_ia, val_va=smua.measure.iv()")
    bottom_source_meter.write("val_pa=smua.measure.p()")
    bottom_current_a = bottom_source_meter.ask("print(val_ia)")
    bottom_voltage_a = bottom_source_meter.ask("print(val_va)")
    bottom_power_a = bottom_source_meter.ask("print(val_pa)")
    print(mapping_dict["bottom_a"], ": bottom_a_power=", bottom_power_a, ", top_a_current=", bottom_current_a, ", bottom_a_voltage=", bottom_voltage_a, sep='')

    # Channel B
    bottom_source_meter.write("smub.measure.autorangei = smub.AUTORANGE_ON")
    bottom_source_meter.write("smub.measure.autorangev = smub.AUTORANGE_ON")
    bottom_source_meter.write("val_ib, val_vb=smub.measure.iv()")
    bottom_source_meter.write("val_pb=smub.measure.p()")
    bottom_current_b = bottom_source_meter.ask("print(val_ib)")
    bottom_voltage_b = bottom_source_meter.ask("print(val_vb)")
    bottom_power_b = bottom_source_meter.ask("print(val_pb)")
    print(mapping_dict["bottom_b"], ": bottom_b_power=", bottom_power_b, ", bottom_b_current=", bottom_current_b, ", bottom_b_voltage=", bottom_voltage_b, sep='')