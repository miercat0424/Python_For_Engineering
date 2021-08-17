from re import I
import nidaqmx 
import time
from nidaqmx.constants import WaitMode
import numpy as np 


with nidaqmx.Task() as task1 :
    
    task1.ao_channels.add_ao_voltage_chan("Dev2/ao0","mychannel",0,5)
    # task2.ao_channels.add_ao_voltage_chan("TC01/ao1","mychannel",0,5)

    count = 0
    
    while count < 1 : 
        
        start = input("Start ? [Y/n]\n")
        if start != "Y" : 
            if start != "n" or "N" :
                print("Wrong Command")
            else :
                print("Stop")
            break
        else :
            pass
        
        for xx in range(3) :
            print(f"Count : {xx+1}")
            time.sleep(1)
        
        result0 = [x for x in np.arange(0,4,0.1)]

        for i in result0 :
            if round(i,1) == 3.9 :
                value = 3.9
                task1.write(value)
                # task2.write(5 - value)
                # task2.write(value)
                print(f"Voltage : {value:.1f} [ V ]")
                time.sleep(1)

                value = 4
                task1.write(value)
                # task2.write(5 - value)
                # task2.write(value)
                print(f"Voltage : {value:.1f} [ V ]\t-Max-\nWaiting...")
                time.sleep(2)
            else :
                value = i 
                task1.write(value)
                # task2.write(5 - value)
                # task2.write(value)
                print(f"Voltage : {value:.1f} [ V ]")
                time.sleep(0.3)

        result1 = [x for x in reversed(np.arange(0,4,0.1))]

        for i in result1 :
            value = i
            task1.write(value)
            # task2.write(5 - value)
            # task2.write(value)
            print(f"Voltage : {value:.1f} [ V ]")
            time.sleep(0.5)

        task1.write(0)
        count += 1

        print(f"[{count}] repeated ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

        
