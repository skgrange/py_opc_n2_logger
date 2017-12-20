# Packages these functions need
import os
import re
from collections import OrderedDict
import time, datetime, pytz
from math import floor


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
  
  # 
  print seconds_to_wait
  
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

