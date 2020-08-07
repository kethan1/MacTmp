# MacTmp

This is a python module used to getting temperatures of the cpu and gpu in Mac OS. If a hardware configurate does not work, make sure to open an issue. 

`pip install MacTmp` for Python2 or `pip3 install MacTmp` for Python3

Please run this with `sudo`

`sudo Python` in Python2 or `sudo Python3` in Python3 

Below is the example code:

```
>>>import MacTmp

>>>print(MacTmp.CPU_Temp()) #To get CPU Temperature

>>>print(MacTmp.GPU_Temp()) #To get GPU Temperature
```

Note: GPU temperature does not work with Intel Integrated Graphics. 

Pypi page here: https://pypi.org/project/MacTmp/

Github Page Here: https://github.com/kethan1/MacTmp/
