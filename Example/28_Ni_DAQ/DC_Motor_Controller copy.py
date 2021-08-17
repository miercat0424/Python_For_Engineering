import nidaqmx 
import time
import numpy as np 


# ----------Devices------------
# USB - 6211 Type DAQ
# L298N Motor Controller
# -----------------------------

with nidaqmx.Task() as task1 , nidaqmx.Task() as task2 , nidaqmx.Task() as task3 , nidaqmx.Task() as task4 :
    task1.do_channels.add_do_chan("Dev2/port1/line0","") # <-- PFI4 OUT port
    task2.do_channels.add_do_chan("Dev2/port1/line1","") # <-- PFI5 OUT port
    task3.do_channels.add_do_chan("Dev2/port1/line2","") # <-- PFI6 OUT port
    task4.do_channels.add_do_chan("Dev2/port1/line3","") # <-- PFI7 OUT port
    
    count = 0

    while count < 1 :

        print("---------------------")
        count += 1 

        
        # PFI4 out --> IN4
        print(f"Motor CW On")
        task1.write(True)
        task3.write(True)
        time.sleep(2)
        # print(f"Motor CW Off")
        task1.write(False)
        task3.write(False)
        # time.sleep(2)

        # PFI5 out --> IN5
        print(f"Motor CCW on")
        task2.write(True)
        task4.write(True)
        time.sleep(2)
        # print(f"Motor CCW off")
        task2.write(False)
        task4.write(False)
        # time.sleep(2)

        print(f"{count} -------------------\n")
    
print("[Done]")