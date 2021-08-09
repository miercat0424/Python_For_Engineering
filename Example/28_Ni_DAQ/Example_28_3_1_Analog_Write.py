import nidaqmx 
import time


with nidaqmx.Task() as task :
    
    task.ao_channels.add_ao_voltage_chan("TC01/ao0","mychannel",0,5)

    count = 0
    
    while True : 

        for i in range(6) :

            if i == 5 :
                value = i 
                task.write(value)
                print(f"Voltage : {value} [ V ]")
                time.sleep(2)
            else :
                value = i 
                task.write(value)
                print(f"Voltage : {value} [ V ]")
                time.sleep(1)

        for i in reversed(range(5)) :
            value = i
            task.write(value)
            print(f"Voltage : {value} [ V ]")
            time.sleep(1)

        count += 1

        print(f"[{count}] repeated ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

        
