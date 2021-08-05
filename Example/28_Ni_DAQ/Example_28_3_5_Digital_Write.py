import nidaqmx 

for _ in range(10) :
        

    with nidaqmx.Task() as task : 
        
        task.do_channels.add_do_chan("TC01/port0/line0")

        value = True
        task.start
        signal = task.write(value)
        print(f"signal : {signal}")
        task.stop()
