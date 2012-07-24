from datetime import datetime

from math import floor

def half_life(file_path, zipcodeflag, stateflag):
  
  f = open(file_path, 'r')
  
  STORYID = 6 - 1 
  TIMEKEYID = 11 - 1 
  ZIPCODE = 44 - 1
  STATE = 38 - 1 
  DELIMITER = '|'

  counter = 1
  ret_array = []
  text = f.next()
  line = text.strip().split(DELIMITER)
  storykey = line[STORYID].strip()
  timekey = line[TIMEKEYID].strip()
  zip_c = line[ZIPCODE].strip()

  timekeys_temp = set().add(timekey)
  zipcodes_temp = set().add(zipcode)
  states_temp = set().add(state)

  tot_counter = 1 
  #iterate over file and return storykey, half_life in hours and number of impressions
  for text in f:
    tot_counter += 1
    line = text.strip().split(DELIMITER)
    storykey_temp = line[STORYID]
    timekey = line[TIMEKEYID].strip()
    zip_c = line[ZIPCODE].strip()
    state_t = line[STATE].strip()

    if storykey_temp == storykey:
      counter += 1
      timekeys_temp.add( timekey )
      zipcodes_temp.add( zip_c )
      states_temp.add( state_t )
    
    else:
      hl_timekey = timekeys_temp[int(floor(counter/2))] 
      half_life =  (datetime.strptime(hl_timekey, '%Y%m%d%H') - datetime.strptime(timekey, '%Y%m%d%H')).seconds/3600
      ret_array = [storykey, half_life, counter]
      if zipcodeflag:
        zip_str = '#'.join(zipcodes_temp)
        ret_array.append(zip_str)
      
      if stateflag:
        state_str = '#'.join(states_temp)
        ret_array.append(state_str)
      
      storykey = storykey_temp
      timekeys_temp = set().add(timekey)
      zipcodes_temp = set().add(zipcode)
      states_temp = set().add(state)
 
      print ret_array ### not sure whether we want to make a matrix of these entries or dump to flatfile 
      counter = 1

  print 'total count: ' + str(tot_counter)    
  f.close()
      
if __name__ == '__main__':
  half_life( '/home/ubuntu/newsright/sorted_impressions_test.csv', zipcode=1, state=1)
