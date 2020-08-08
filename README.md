# MacTmp

This is a python module used to getting temperatures of the cpu and gpu in Mac OS. If a hardware configurate does not work, make sure to open an issue. 

Python2 Installation: `pip install MacTmp`

Python3 Installation: `pip3 install MacTmp`

Please run this with `sudo`

Python2: `sudo python`

Python3: `sudo python3`

Below is the example code:

```
>>>import MacTmp

>>>print(MacTmp.CPU_Temp()) #To get CPU Temperature

>>>print(MacTmp.GPU_Temp()) #To get GPU Temperature
```

Both temperatures are in celcius. 

Note: GPU temperature does not work with Intel Integrated Graphics. 

Pypi page here: https://pypi.org/project/MacTmp/

Github Page Here: https://github.com/kethan1/MacTmp/
