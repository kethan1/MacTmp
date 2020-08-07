import os

# ioreg -l |grep \"PerformanceStatistics\" | cut -d '{' -f 2 | tr '|' ',' | tr -d '}' | tr ',' '\n'|grep 'Temp\|Fan\|Clock'; done

def CPU_Temp():
    tmp = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
    return tmp[12].strip('CPU die temperature: ')

def GPU_Temp():
    return [i.strip('GPU die temperature: ' for i in os.popen('sudo powermetrics|grep -i "GPU die temperature"').readlines())]
