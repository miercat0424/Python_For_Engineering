import nidaqmx

for _ in range(10) :
    
    with nidaqmx.Task() as task :
        
        task.ai_channels.add_ai_voltage_chan("TC01/ai0", min_val=0 , max_val=10)

        value = task.read()
        print(value)

        task.stop

