import sys

import csv



def printCat(file_path, header):
      
    f = open(file_path, 'r')
    if header:
        head = f.readline()
        
    STORYID = 1 - 1 
    CATEGORY = 2 - 1 
    DELIMITER = '|'
   
    text = f.readline() 
    pointer = f.tell()

    line = text.strip().split(DELIMITER)
    storykey = line[STORYID].strip()
    f.seek(pointer)
           
    CategorySet = set()
    
    tot_counter = 0

    for text in f:
        tot_counter += 1
        
        line = text.strip().split(DELIMITER)
        storykey_temp = line[STORYID].strip()
        cat = line[CATEGORY].strip()
          
        if storykey_temp != storykey:
            cat_str = '#'.join(CategorySet)
            print ','.join([storykey, cat_str])
            storykey = storykey_temp
            CategorySet = set()
        
        CategorySet.add( cat )
                
    print ','.join([storykey, cat_str])
      
    #print 'total count: ' + str(tot_counter)    
    f.close()
    #g.close()
      
if __name__ == '__main__':    
    printCat('/home/ubuntu/newsright/halflifedata/story_category_run1.csv', header=1)

