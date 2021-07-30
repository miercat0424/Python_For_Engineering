import nidaqmx
import time

task = nidaqmx.Task()

aa = task.ai_channels.add_ai_thrmcpl_chan("TC01/ai0")

N = 5
Time_sleep = 1

task.start()

for k in range(N) :

    value = round(task.read(),1)
    print(f"ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\
    task.ai_channels : {aa}\n\n\
    value : \t{value}\n\
    task  : \t{task}")
    time.sleep(Time_sleep)

task.stop()
task.close()
