import time
import nidaqmx 


with nidaqmx.Task() as task : 
    
    task.do_channels.add_do_chan("TC01/port0/line0")

    value = True
    task.start
    
    i = 0                       # Times
    
    while i < 10 :
        
        print(i)
        
        task.write(value)       # turn on
        
        time.sleep(0.5)         # time delay

        value = not value       # turn off

        task.write(value)       # turn on 

        i += 1 

    task.stop
