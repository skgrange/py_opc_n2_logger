# Packages these functions need
import os
import re
from collections import OrderedDict
import time, datetime, pytz
from math import floor
import argparse
import gc
import pandas as pd


# Function to sleep until the start of the next minute. 
# 
# Used for clean starting of log files.
def nice_starter(verbose = True):
  
  # Get time
  date_run = datetime.datetime.utcnow()
  
  # Get time to start
  date_to_start = 60 - (date_run.second + date_run.microsecond / 1000000.0)
  
  if verbose:
    
    print '\nWaiting until the beginning of the next minute (' + \
      str(int(date_to_start)) + ' seconds) before starting logging...'
    
  # Sleep until future
  time.sleep(date_to_start)
  

# Function to sleep until the next clean time period. 
#
# Used at the end of a process. 
def nice_waiter(frequency):
  
  # Find current time
  date_now = time.time()
  
  # When should the need iteration be? 
  date_next = floor(date_now) + int(frequency)
  
  # Find the time to wait
  seconds_to_wait = date_next - time.time()
  
  # Ensure date is nice and clean, if not fix it
  date_modulo = date_next % int(frequency)
  
  if date_modulo == 0:
    
    pass
  
  else:
    
    # Reassign to clean date
    date_next = date_next - date_modulo

  seconds_to_wait = date_next - time.time()
  
  # print seconds_to_wait
  
  # Sleep until the clean time
  time.sleep(seconds_to_wait)


def clean_histogram_return(dict): 
  
  # Lower case keys
  dict = {k.lower(): v for k, v in dict.items()}
  
  # Clean names
  # Replace spaces
  dict = {k.replace(' ', '_'): v for k, v in dict.items()}
  
  # Regular expression replacements
  dict = {re.sub('bin_0$', 'bin_00', k): v for k, v in dict.items()}
  dict = {re.sub('bin_1$|bin1', 'bin_01', k): v for k, v in dict.items()}
  dict = {re.sub('bin_2$', 'bin_02', k): v for k, v in dict.items()}
  dict = {re.sub('bin_3$|bin3', 'bin_03', k): v for k, v in dict.items()}
  dict = {re.sub('bin_4$', 'bin_04', k): v for k, v in dict.items()}
  dict = {re.sub('bin_5$|bin5', 'bin_05', k): v for k, v in dict.items()}
  dict = {re.sub('bin_6$', 'bin_06', k): v for k, v in dict.items()}
  dict = {re.sub('bin_7$|bin7', 'bin_07', k): v for k, v in dict.items()}
  dict = {re.sub('bin_8$', 'bin_08', k): v for k, v in dict.items()}
  dict = {re.sub('bin_9$', 'bin_09', k): v for k, v in dict.items()}
  
  # Order by key, alphabetical
  dict = OrderedDict(sorted(dict.items(), key = lambda t: t[0]))
  
  return dict
  

def create_directory(directory_output): 

  if not os.path.exists(directory_output):
  
    os.makedirs(directory_output)
  
  else: 
  
    pass


def date_unix(integer = False):
	
  # Get date
  date = time.time()

  # Data type
  if integer: 
	  
    date = floor(date)
    date = int(date)
    
  else:
	  
    pass

  return date


def catch_arguments(): 
  
  # Command line arguments
  parser = argparse.ArgumentParser()
  
  # The arguments
  parser.add_argument(
    '-o', 
    '--output', 
    default = '~/Desktop/data', 
    help = 'Which directory should be used to export the programme\'s data files \
    too?'
  )
  
  parser.add_argument(
    '-d', 
    '--device', 
    default = '/dev/ttyACM0', 
    help = 'What is the device/location is the Alphasense OPC-N2 sensor?'
  )
  
  parser.add_argument(
    '-tz', 
    '--time_zone', 
    default = 'UTC',
    help = 'Which time zone will the date be stored in? As an Olison time-zone \
    string. Epoch time is also stored so time-zone information can always be \
    found from the data files.'
  )
  
  # Add arguments to object to be called in programme
  args = parser.parse_args()
  
  # Modify file directory so ~ can be used  
  args.output = os.path.expanduser(args.output)
  
  # If the output directory does not exist, create it
  create_directory(args.output)
  
  return args
 
 
def housekeeping():

  # Garbage collection
  if datetime.datetime.fromtimestamp(time.time()).minute % 15 == 0:
  
    gc.collect()
	
  else:
  
    pass  


def get_measurements(sensor, time_zone, serial_number): 
  
  # Get measurement date
  date = time.time()
  
  # Used for logging and other data export things but not logic
  date_floor = floor(date)
  
  # Make a date string
  date_string = datetime.datetime.fromtimestamp(
    date_floor,
    pytz.timezone(time_zone)
  ).strftime('%Y-%m-%d %H:%M:%S %Z')
  
  # Day string for files
  day_string = datetime.datetime.fromtimestamp(
    date,
    pytz.timezone('UTC')
  ).strftime('%Y-%m-%d')
  
  # Create an extra dictionary
  dict_extra = OrderedDict([
    ('sensor', serial_number), 
    ('date', date_string),
    ('date_unix', date_floor)
  ])
  
  # Get sensor reponses
  # Get histogram response
  dict_bins = sensor.histogram()
  
  # Clean dictionary
  dict_bins = clean_histogram_return(dict_bins)
  
  # Sensor needs some time between querries to avoid errors
  time.sleep(0.2)
  
  # Get particulate bins response
  dict_pm = sensor.pm()
  
  # Lower case keys
  dict_pm = {k.lower(): v for k, v in dict_pm.items()}
  
  # Bind dictonaries together
  dict_bind = OrderedDict(
    list(dict_extra.items()) + 
    list(dict_pm.items()) + 
    list(dict_bins.items())
  )
  
  return(dict_bind)



def aggregate_measurements(list_results, round = True):
  
  # To data frame  
  df = pd.DataFrame(list_results)
  
  # Force data types, missing data really here
  df['temperature'] = df['temperature'].astype(float)
  df['pressure'] = df['pressure'].astype(float)
  
  # Aggregate by sensor
  df_group = df.groupby(by = 'sensor')
  df_group = df_group.mean()
  
  # Round numeric variables
  if round:
  
    df_group = df_group.round(decimals = 3)
	
  else: 
  
    pass
  
  # Overwrite some variables
  # First observation for minute
  df_group['date'] = df.date[0]
  df_group['date_unix'] = df.date_unix[0]
  df_group['checksum'] = df.checksum[0]
  
  # Duplicated data, but easier
  df_group['sensor'] = df.sensor[0]
  
  # Order variables
  df_group = df_group[list_results[0].keys()]
  
  return(df_group)


# Function to write data frame to disk
def write_sensor_data(df, directory):

  # Create file name
  file_name = df.date[0].split(' ')[0] + '_alphasense_opc_n2_data.csv'
  
  # Add directory
  file_name = os.path.join(directory, file_name)
  
  # File writer
  if not os.path.isfile(file_name): 
    
    # If file does not exist, create and add header
    df.to_csv(file_name, index = False)
    
  else: 
    
    # If file exists, append and do not write header
    df.to_csv(file_name, index = False, mode = 'a', header = False)
    
  # No return
