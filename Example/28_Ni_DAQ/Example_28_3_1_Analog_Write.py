import nidaqmx 

with nidaqmx.Task() as task :
    
    task.ao_channels.add_ao_voltage_chan("TC01/ao0","mychannel",0,5)

    value = 4
    task.start
    signal = task.write(value)
    print(f"Signal  : {signal} [ I|O ]\
        \nVoltage : {value} [ V ]")
    task.stop
