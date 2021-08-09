import nidaqmx 

with nidaqmx.Task() as task : 
    
    task.do_channels.add_do_chan("TC01/port0/line0")

    value = True
    print(task.write(value))
    # task.start
    # task.stop()
