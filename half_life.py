from datetime import datetime
from math import floor

def half_life(file_path):
  
  f = open(file_path, 'r')
  
  STORYID = 6 - 1 
  TIMEKEYID = 11 - 1 
  DELIMITER = '|'

  counter = 1
  ret_array = []
  text = f.next()
  line = text.strip().split(DELIMITER)
  storykey = line[STORYID]
  timekey = line[TIMEKEYID]
  timekeys_temp = [timekey]
  storykey = -1

  #iterate over file and return storykey, half_life in hours and number of impressions
  for text in f:
    line = text.strip().split(DELIMITER)
    storykey_temp = line[STORYID]

    if storykey_temp == storykey:
      counter += 1
      timekeys_temp.append(line[TIMEKEYID])
    else:
      hl_timekey = timekeys_temp[int(floor(counter/2))] 
      half_life =  (datetime.strptime(hl_timekey, '%Y%m%d%H') - datetime.strptime(timekey, '%Y%m%d%H')).seconds/3600
      ret_array = [storykey, half_life, counter]
      
      storykey = storykey_temp
      timekey = line[TIMEKEYID]
      timekeys_temp = [timekey]
      counter = 1
      print ret_array ### not sure whether we want to make a matrix of these entries or dump to flatfile 
      ret_array = []
      
  f.close()
      
if __name__ == '__main__':
  half_life( '/home/ubuntu/newsright/sorted_impressions_test.csv')
