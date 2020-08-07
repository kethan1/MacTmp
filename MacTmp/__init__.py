import os

def CPU_Temp():
    return [i.strip('CPU die temperature') for i in os.popen('sudo powermetrics|grep -i "CPU die temperature"').readlines()]

def GPU_Temp():
    return [i.strip('GPU die temperature: ' for i in os.popen('sudo powermetrics|grep -i "GPU die temperature"').readlines())]
