from datetime import datetime
from math import floor

def half_life(file_path):
  
  f = open(file_path, 'r')
  
  STORYID = 6 
  TIMEKEYID = 11 
  DELIMITER = '|'

  counter = 1
  timekeys_temp = []
  ret_array = []
  storykey = -1

  #iterate over file and return storykey, half_life in hours and number of impressions
  for text in f:
    line = text.strip().split(DELIMITER)
    storykey_temp = line[STORYID]

    if counter == 1:
      storykey = storykey_temp
      timekeys_temp.append(line[TIMEKEYID])
      counter += 1
      next
    if storykey_temp == storykey:
      counter += 1
      timekeys_temp.append(line[TIMEKEYID])
    else:
      hl_timekey = timekeys_temp[int(floor(counter/2))] 
      half_life =  (datetime.strptime(hl_timekey, '%Y%m%d%H') - datetime.strptime(timekey, '%Y%m%d%H')).seconds/3600
      ret_array.append(storykey, half_life, counter)  
      
      storykey = storykey_temp
      timekey = line[TIMEKEYID]
      counter = 1
      print ret_array ### not sure whether we want to make a matrix of these entries or dump to flatfile 
      ret_array = []
      
  f.close()
      
if __name__ == '__main__':
  half_life( '/home/ubuntu/newsright/sorted_impressions_test.csv')
