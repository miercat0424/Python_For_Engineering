from re import I
import nidaqmx 
import time
import numpy as np 


with nidaqmx.Task() as task1 , nidaqmx.Task() as task2 :
    
    task1.ao_channels.add_ao_voltage_chan("TC01/ao0","mychannel",0,5)
    task2.ao_channels.add_ao_voltage_chan("TC01/ao1","mychannel",0,5)

    count = 0
    
    while True : 

        result0 = [x for x in np.arange(0,5,0.1)]
        for i in result0 :
            
            if i == 4.9 :
                value = 4.9
                task1.write(value)
                # task2.write(5 - value)
                task2.write(value)
                print(f"Voltage : {value:.1f} [ V ]")
                time.sleep(1)

                value = 5
                task1.write(value)
                # task2.write(5 - value)
                task2.write(value)
                print(f"Voltage : {value:.1f} [ V ]\t-Max-\nWaiting...")
                time.sleep(2)
            else :
                value = i 
                task1.write(value)
                # task2.write(5 - value)
                task2.write(value)
                print(f"Voltage : {value:.1f} [ V ]")
                time.sleep(0.3)

        result1 = [x for x in reversed(np.arange(0,5,0.1))]

        for i in result1 :
            value = i
            task1.write(value)
            # task2.write(5 - value)
            task2.write(value)
            print(f"Voltage : {value:.1f} [ V ]")
            time.sleep(0.5)

        count += 1

        print(f"[{count}] repeated ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

        
