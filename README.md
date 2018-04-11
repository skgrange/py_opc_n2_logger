# pylogger_opc_n2 

## Please note

This package is now deprecated. The dependencies have been updated and these programmes need to be enhanced to handle these changes. I do not have the hardware at the moment to do this development so this package will not be useful. 

**pylogger_opc_n2** is a data logging package for the [Alphasense's OPC-N2](http://www.alphasense.com/index.php/products/optical-particle-counter/) particle sensor. It is built upon [**py-opc**](http://py-opc.readthedocs.io) and [**pyusbiss**](https://github.com/DancingQuanta/pyusbiss). **pylogger_opc_n2** interacts with the sensor with the USB interface via **pyusbiss** and works well on a Raspberry Pi running a Debian-based Linux distribution. 

By default, the programme assumes the sensor is located at `/dev/ttyACM0`, will query the sensor every five seconds and aggregate every minute, and will use the `~/Desktop/data` as the directory to save observations. The data files have been designed for clarity and ease of use and are suitable for further analyses. 

## Installation

Python, pip, [**pyusbiss**](https://github.com/DancingQuanta/pyusbiss), and **pylogger_opc_n2** will need to be installed.

```
# Install pyusbiss from github, a dependency
pip install git+https://github.com/DancingQuanta/pyusbiss

# Install pylogger_opc_n2
pip install git+https://github.com/skgrange/py_opc_n2_logger
```

If installing on a Raspberry Pi, the installation of Pandas is very slow due to the compilation. You can drop the pandas entry in `setup.py` if pandas is already installed to speed things up. 

If you encounter issues, ensure that your system repositories are up to date with `sudo apt get update` and if the `python-dev` development packages are missing, install them with `sudo apt install python-dev`. 

## Set-up

  1. Install the packages. 
  
  2. Find where the sensor is:

```
# Where is the device?
dmesg | grep tty
# Will probably be ttyACM0
```

  3. Ensure your user is in the `dialout` group, this allows a user to read and write to serial ports:
  
```
# Add user to the dialout group, change `user_name`
# sudo adduser user_name dialout
```

  4. Wait for a minute or so after the sensor's fan starts to operate. If the sensor is attempted to be queried before it is ready, it will not respond. 

  5. Run the logging programme: 
  
```
# Start logging data from the sensor, it is installed as a system programme
alphasense_opc_n2_logger
```

The programme arguments allow for the device/location such as `ttyACM0`, the output directory of the data files (the default is `~/Desktop/data`), and the time zone used for the data files to be specified (the default is "UTC"). Run `alphasense_opc_n2_logger --help` to find some help information about these arguments. 

  6. Use the `.csv` data files for something interesting. 

## To-do 

   - Allow for different sensor query frequency and aggregation periods.
   
   - Drop Pandas as a dependency. The install of Pandas takes far too long on Raspberry Pi computers to compile and install. 
