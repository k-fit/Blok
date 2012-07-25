from datetime import datetime

from math import floor

def printStoryInfo(storykey, timekeysList, zipcodeSet, stateSet, zipcodeflag, stateflag):
    counter = len(timekeysList)
    halflife_time = timekeysList[int( floor (counter / 2 ))]
    
    half_life =  (datetime.strptime(halflife_time, '%Y%m%d%H') - datetime.strptime(timekeysList[0], '%Y%m%d%H'))   
    half_life = half_life.total_seconds()
    half_life = half_life / 3600

    output = [storykey, counter, half_life]
    
    if zipcodeflag:
        zip_str = '#'.join(zipcodeSet)
        output.append(zip_str)
    
    if stateflag:
        state_str = '#'.join(stateSet)
        output.append(state_str)
    
    return output


def half_life(file_path, zipcodeflag, stateflag):
  
    f = open(file_path, 'r')

    STORYID = 6 - 1 
    TIMEKEYID = 11 - 1 
    ZIPCODE = 44 - 1
    STATE = 38 - 1 
    DELIMITER = '|'

    pointer = f.tell()
    text = f.next()
    line = text.strip().split(DELIMITER)
    storykey = line[STORYID].strip()
    f.seek(pointer)

    timekeysList = [] 
    zipcodeSet = set()
    stateSet = set()

    tot_counter = 0
#iterate over file and return storykey, half_life in hours and number of impressions
    for text in f:
        tot_counter += 1
        
        line = text.strip().split(DELIMITER)
        storykey_temp = line[STORYID].strip()
        timekey = line[TIMEKEYID].strip()
        zip = line[ZIPCODE].strip()
        state = line[STATE].strip()
        
        if storykey_temp != storykey:
            print printStoryInfo(storykey, timekeysList, zipcodeSet, stateSet, zipcodeflag, stateflag)
            storykey = storykey_temp
            timekeysList = []
            zipcodeSet = set()
            stateSet = set()
            
        timekeysList.append( timekey )
        if zip: zipcodeSet.add( zip )
        if state: stateSet.add( state )
    
    print printStoryInfo(storykey, timekeysList, zipcodeSet, stateSet, zipcodeflag, stateflag)
       
    print 'total count: ' + str(tot_counter)    
    f.close()
      
if __name__ == '__main__':
      half_life( 'sorted_impressions_test.csv', zipcodeflag = 1, stateflag = 1)
