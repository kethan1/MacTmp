# MacTmp

This is a python module used to find the temperatures of the CPU and GPU in Mac OS. If there is an issue with this module, please open an issue. 

Python2 Installation: `pip install MacTmp`

Python3 Installation: `pip3 install MacTmp`

Please run this with `sudo`

Python2: `sudo python`

Python3: `sudo python3`

Below is the example code:

```python
>>>import MacTmp

>>>print(MacTmp.CPU_Temp()) #To get CPU Temperature

>>>print(MacTmp.GPU_Temp()) #To get GPU Temperature
```

Both temperatures are in Celcius. 

Note: GPU temperature does not work with Intel Integrated Graphics. 

PyPI page here: https://pypi.org/project/MacTmp/

Github Page Here: https://github.com/kethan1/MacTmp/
