import nidaqmx
import numpy as np 
import time
 

from nidaqmx.constants import TerminalConfiguration

Vin = 5 
Ro = 10000 # %10k Resister

with nidaqmx.Task() as task : 
    
    task.ai_channels.add_ai_voltage_chan("TC01/ai0",terminal_config = TerminalConfiguration.RSE)

    i = 0 

    while i < 10 :

        Vout = task.read()

        # Voltage Divider Equation
        # Rt = 10000 // Used fro testing . Setting Rt = 10k shoud gitve TempC = 25
        Rt = (Vout*Ro)/(Vin-Vout)

        # Steinhart constatns
        A = 0.001129148
        B = 0.000234125
        C = 0.0000000876741

        # Steinhart - Hart Equation
        TempK = 1/ (A + (B * np.log(Rt)) + (C * pow(np.log(Rt),3) ) )

        # Convert from Kelvin to Celsius
        TempC = TempK - 273.15

        print(f"Sample : {i}\
        \nVoltage Value : {round(Vout,2)}\
        \nCelsius Value : {round(TempC,1)}\
        \n-----------------------------------------")

        time.sleep(0.5)

        i += 1

    task.stop