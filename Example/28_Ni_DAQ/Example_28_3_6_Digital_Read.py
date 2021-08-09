import nidaqmx

# for _ in range(10) :

with nidaqmx.Task() as task : 

    task.di_channels.add_di_chan("TC01/port0/line1")
    
    task.start
    value = task.read()
    print(value)
    task.stop
