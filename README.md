# pylogger_opc_n2 

**pylogger_opc_n2** is a data logging Python package for the [Alphasense's OPC-N2](http://www.alphasense.com/index.php/products/optical-particle-counter/) particle sensor. It is built upon [**py-opc**](http://py-opc.readthedocs.io) and [**pyusbiss**](https://github.com/DancingQuanta/pyusbiss). **pylogger_opc_n2** interacts with the sensor with the USB interface. 

## Installation

Both [**pyusbiss**](https://github.com/DancingQuanta/pyusbiss) and **pylogger_opc_n2** will need to be installed. 

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
# Add user to the dialout group, change user_name
# sudo adduser user_name dialout
```
  
## To-do 
 
  - Argument passing
    - Device address
    - Output directory
    
  - Garbage collection
  
  - Functionality to aggregate observations