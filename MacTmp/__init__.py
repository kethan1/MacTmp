import os

# ioreg -l |grep \"PerformanceStatistics\" | cut -d '{' -f 2 | tr '|' ',' | tr -d '}' | tr ',' '\n'|grep 'Temp\|Fan\|Clock'; done

def CPU_Temp():
    tmp = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
    for each in tmp:
        if 'CPU die temperature' in tmp:
            return each.strip('CPU die temperature: ')
    return 'CPU Temperature not found'

def GPU_Temp():
    # Will not work with Integrated Intel Gpu
    tmp = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
    for each in tmp:
        if 'GPU die temperature' in tmp:
            return each.strip('GPU die temperature: ')
    return 'GPU Temperature not found'