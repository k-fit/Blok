from datetime import datetime

from math import floor

import sys

import csv

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


def half_life(file_path, zipcodeflag, stateflag, header):
      
    f = open(file_path, 'r')
    
    #skip header 
    if header:
        head = f.next()
        
    
    g = open('half_life_run1.txt', 'w')

    STORYID = 1 - 1 
    TIMEKEYID = 2 - 1 
    ZIPCODE = 3 - 1
    #STATE = 38 - 1 
    DELIMITER = '|'

   
    text = f.next()
    if header:
        pointer = len(head)
    else:
        pointer = len(text)

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
        
       # if tot_counter ==10000:
        #    sys.exit()
         #   g.close()
          #  f.close()

        line = text.strip().split(DELIMITER)
        storykey_temp = line[STORYID].strip()
        timekey = line[TIMEKEYID].strip()
        if zipcodeflag: zip = line[ZIPCODE].strip()
        if stateflag: state = line[STATE].strip()
          
        if storykey_temp != storykey:
            #print printStoryInfo(storykey, timekeysList, zipcodeSet, stateSet, zipcodeflag, stateflag)
            csv.writer(g).writerow(printStoryInfo(storykey, timekeysList, zipcodeSet, stateSet, zipcodeflag, stateflag))
            storykey = storykey_temp
            timekeysList = []
            zipcodeSet = set()
            stateSet = set()
            
        timekeysList.append( timekey )
        if zipcodeflag and zip: zipcodeSet.add( zip )
        if stateflag and state: stateSet.add( state )
    
    #print printStoryInfo(storykey, timekeysList, zipcodeSet, stateSet, zipcodeflag, stateflag)
    csv.writer(g).writerow(printStoryInfo(storykey, timekeysList, zipcodeSet, stateSet, zipcodeflag, stateflag))
      
    print 'total count: ' + str(tot_counter)    
    f.close()
    g.close()
      
if __name__ == '__main__':
     # half_life( 'sorted_impressions_test.csv', zipcodeflag = 1, stateflag = 0)
      half_life('/mnt/data.csv', zipcodeflag = 1, stateflag = 0, header=1)
