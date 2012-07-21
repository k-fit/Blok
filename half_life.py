from datetime import datetime
from math import floor


def half_life(file_url):
  
  f = open(file_url, 'r')
  

  counter = 1
  timekeys_temp = []
  ret_array = []

  ### get relevant data from first line 
  first_line = f.next()
  storykey = first_line[6[
  timekey = first_line[11]

  #iterate over file and return storykey, half_life in hours and number of impressions
  for line in f:
    storykey_temp = line[6]

    if storykey_temp == storykey:
      counter += 1
      timekeys_temp.append(line[11]
    else:
      hl_timekey = timekeys_temp[int(floor(counter/2))] 
      half_life =  (datetime.strptime(hl_timekey, '%Y%m%d%H') - datetime.strptime(timekey, '%Y%m%d%H')).seconds/3600
      ret_array.append(storykey, half_life, counter)  
      
      storykey = storykey_temp
      timekey = line[11]
      counter = 1
      
      print ret_array ### not sure whether we want to make a matrix of these entries or dump to flatfile 

      ret_array = []
      
    f.close()
      

