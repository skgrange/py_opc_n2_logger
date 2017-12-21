# pylogger_opc_n2 

**pylogger_opc_n2** is a data logging package for the [Alphasense's OPC-N2](http://www.alphasense.com/index.php/products/optical-particle-counter/) particle sensor. It is built upon [**py-opc**](http://py-opc.readthedocs.io) and [**pyusbiss**](https://github.com/DancingQuanta/pyusbiss). **pylogger_opc_n2** interacts with the sensor with the USB interface via **pyusbiss** and works well on a Raspberry Pi running a Debian-based Linux distribution. 

## Installation

Python, pip, [**pyusbiss**](https://github.com/DancingQuanta/pyusbiss), and **pylogger_opc_n2** will need to be installed.

```
# Install pyusbiss from github, a dependency
pip install git+https://github.com/DancingQuanta/pyusbiss

# Install pylogger_opc_n2
pip install git+https://github.com/skgrange/py_opc_n2_logger
```

## Set-up

  1. Install the packages. 
  
  2. Find where the sensor is:

```
# Where is the device?
dmesg | grep tty
# Should be ttyACM0
```

  3. Ensure your user is in the `dialout` group:
  
```
# Add user to the dialout group, change `user_name`
# sudo adduser user_name dialout
```

  4. Run logging programme: 
  
```
# Start logging data from the sensor, installed as a system programme
alphasense_opc_n2_logger
```

  5. Use the `.csv` data files for something interesting 
  
## To-do 
 
  - Argument passing
  
    - Device addresses
    - Output directory
    - Sensor query frequency
    
  - Garbage collection
  
  - Functionality to aggregate observations
