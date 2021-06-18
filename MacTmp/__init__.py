import os

def CPU_Temp():
    cpu_temp = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
    for line in cpu_temp:
        if 'CPU die temperature' in line:
            return line.strip('CPU die temperature: ').rstrip(' C')
    return 'CPU Temperature not found'

def GPU_Temp():
    # Will not work with Integrated Intel GPU
    gpu_temp = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
    for line in gpu_temp:
        if 'GPU die temperature' in line:
            return line.strip('GPU die temperature: ').rstrip(' C')
    return 'GPU Temperature not found'

if __name__ == '__main__':
    print(CPU_Temp())
    print(GPU_Temp())
