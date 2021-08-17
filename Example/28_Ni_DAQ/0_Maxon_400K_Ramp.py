from re import I
import nidaqmx 
import time
from nidaqmx import task
from nidaqmx.constants import WaitMode
import numpy as np 


with nidaqmx.Task() as task1 :
    
    task1.ao_channels.add_ao_voltage_chan("Dev2/ao0","mychannel",-10,10)
    task1.write(0)
    count = 0
    
    while count < 1 : 
        
        start = input("Start ? [Y/n]\t")
        if start != "Y" : 
            if start != "n" and start != "N" :
                print("Wrong Command")
            else :
                print("Stop")
            break
        else :
            pass


        for times in range(5) :

            for i in range(4) :
                task1.write(2)
                time.sleep(0.1)
                task1.write(-2)
                time.sleep(0.1)

            for i in range(1) :
                task1.write(10)
                time.sleep(0.5)
                task1.write(-10)
                time.sleep(0.5)
            
            print(5 - (times+1) , " times left")


        task1.write(0)
        count += 1

        print(f"[{count}] repeated ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

        
