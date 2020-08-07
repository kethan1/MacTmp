import os

def CPU_Temp():
    return os.popen('sudo powermetrics|grep -i "CPU die temperature"').strip('CPU die temperature: ')

def GPU_Temp():
    return os.popen('sudo powermetrics|grep -i "GPU die temperature"').strip('GPU die temperature: ')
