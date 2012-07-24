from datetime import datetime

from math import floor

def half_life(file_path, zipcode, state):
  
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
  storykey = line[STORYID]
  timekey = line[TIMEKEYID]
  timekeys_temp = [timekey]
  zip_c = line[ZIPCODE]
  zipcodes_temp = [str(zipcode)]
  states_temp = [str(state)]
  storykey = -1
 
  tot_counter = 1
  #iterate over file and return storykey, half_life in hours and number of impressions
  for text in f:
    tot_counter += 1
    line = text.strip().split(DELIMITER)
    storykey_temp = line[STORYID]

    if storykey_temp == storykey:
      counter += 1
      timekeys_temp.append(line[TIMEKEYID])
      if zipcode:
        zipcodes_temp.append(str(line[ZIPCODE]))
      if state:
	states_temp.append(str(line[STATE]))
    else:
      hl_timekey = timekeys_temp[int(floor(counter/2))] 
      half_life =  (datetime.strptime(hl_timekey, '%Y%m%d%H') - datetime.strptime(timekey, '%Y%m%d%H')).seconds/3600
      if zipcode:
	zip_str = '#'.join(list(set(zipcodes_temp)))
        if len(zip_str)>0 and zip_str[0]=='#': zip_str = zip_str[1:]
	#for z in list(set(zipcodes_temp)):
	 # zip_str = zip_str + str(z) + "#"
     	ret_array = [storykey, half_life, counter, zip_str]
 
      if state:
        state_str = '#'.join(set(states_temp))
        if len(state_str)> 0 and state_str[0] == '#': state_str = state_str[1:]
        #for s in list(set(states_temp)):
	 # state_str = state_str + str(s) + "#"
        ret_array = [storykey, half_life, counter, state_str]

      if zipcode and state:
        ret_array = [storykey, half_life, counter, zip_str, state_str]

      if not zipcode and not state:		   
        ret_array = [storykey, half_life, counter]
      
      storykey = storykey_temp
      timekey = line[TIMEKEYID]
      timekeys_temp = [timekey]
      zip_c = line[ZIPCODE]
      zipcodes_temp = [zip_c]
      state_t = line[STATE]
      states_temp = [state_t]  
      print ret_array ### not sure whether we want to make a matrix of these entries or dump to flatfile 
      counter = 1
      ret_array = []

  print 'total count: ' + str(tot_counter)    
  f.close()
      
if __name__ == '__main__':
  half_life( '/home/ubuntu/newsright/sorted_impressions_test.csv', zipcode=1, state=1)
