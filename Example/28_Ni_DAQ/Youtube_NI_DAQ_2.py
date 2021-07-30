import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

#   Initialize Logging
Tstop   =   20              #Logging Time [sec]
Ts      =   0.5
N       =   int(Tstop/Ts)
data    =   []

#   Initialize DAQ Device
task    =   nidaqmx.Task()
task.ai_channels.add_ai_thrmcpl_chan("TC01/ai0")
task.start()

#   Logging Temperature Data from DAQ Device
for k in range(N):
    value = task.read()
    print(f"T = {round(value,1)}\t[ deg C ]")
    data.append(value)
    time.sleep(Ts)

task.stop()
task.close()

#   Plotting 
t = np.arange(0,Tstop,Ts)

Tmin = -150
Tmax = 150

plt.plot(t,data,"-o")
plt.title("Temperature")
plt.xlabel("t [s]")
plt.ylabel("Temp [degC]")
plt.grid()
plt.axis([0,Tstop,Tmin,Tmax])
plt.show()