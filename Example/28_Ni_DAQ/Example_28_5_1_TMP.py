import nidaqmx
import time

from nidaqmx.constants import ( TerminalConfiguration )

with nidaqmx.Task() as task : 
    
    task.ai_channels.add_ai_voltage_chan("TC01/ai0",terminal_config = TerminalConfiguration.RSE)

    i = 0

    while i < 10 :

        voltage = task.read()

        degressC = 100 * voltage - 50 

        print(f"Sample : {i}\
            \nVoltage Value : {round(voltage,2)} [V]\
            \nCelsius Value : {round(degressC,1)} [C]\
            \nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        
        time.sleep(0.5)

        i += 1

    task.stop