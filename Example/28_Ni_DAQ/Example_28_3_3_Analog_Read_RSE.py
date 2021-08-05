import nidaqmx 

from nidaqmx.constants import (TerminalConfiguration)

for _ in range(10) : 
    
    with nidaqmx.Task() as task :
        
        task.ai_channels.add_ai_voltage_chan("TC01/ai0",terminal_config=TerminalConfiguration.RSE)

        value = task.read()
        print(value)
        task.stop

    
