# MacTmp

This is a python module used to find the temperatures of the CPU and GPU in Mac OS. If there is an issue with this module, please open an issue. 

Installation: `pip3 install MacTmp`

## Usage in CLI

```shell
~ mactmp --help
usage: mactmp [-h] [-c] [-g] [-a]

Get CPU and GPU Temperature

optional arguments:
  -h, --help  show this help message and exit
  -c, --cpu   Get CPU Temperature
  -g, --gpu   Get GPU Temperature
  -a, --all   Get CPU and GPU Temperature

```

## Usage in code

Please run this with `sudo`

Run: `sudo python3 file.py`

Below is the example code:

```python3
>>> import MacTmp
>>> print(MacTmp.CPU_Temp())  # To get CPU Temperature
>>> print(MacTmp.GPU_Temp())  # To get GPU Temperature
```

Both temperatures are in Celsius. 

Note: GPU temperature does not work with Intel Integrated Graphics. This module doesn't work with Mac Mini's, and support for M1 Macs is untested. This module relies on `powermetrics`, so if that command works, this module should work. 

PyPI page here: https://pypi.org/project/MacTmp/

Github Page Here: https://github.com/kethan1/MacTmp/
