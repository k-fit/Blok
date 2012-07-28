import sys

import csv



def printCat(file_path, file_path_out, header):
      
    f = open(file_path, 'r')
    
    #skip header 
    if header:
        head = f.next()
        
    
    g = open(file_path_out, 'w')

    STORYID = 1 - 1 
    CATEGORY = 2 - 1 
    DELIMITER = '|'

   
    text = f.next()
    if header:
        pointer = len(head)
    else:
        pointer = len(text)

    line = text.strip().split(DELIMITER)
    storykey = line[STORYID].strip()
    f.seek(pointer)
           
    CategorySet = set()
    
    tot_counter = 0
#iterate over file and return storykey, half_life in hours and number of impressions
    for text in f:
        tot_counter += 1
        
        #if tot_counter ==10:
         #   sys.exit()
          #  g.close()
           # f.close()

        line = text.strip().split(DELIMITER)
        storykey_temp = line[STORYID].strip()
        cat = line[CATEGORY].strip()
          
        if storykey_temp != storykey:
	        #cat_str = '#'.join(CategorySet)
            cat_str = '#'.join(CategorySet)
            #print [storykey, cat_str]
            csv.writer(g).writerow([storykey, cat_str])
            storykey = storykey_temp
            CategorySet = set()
        
        CategorySet.add( cat )
                
    #print [storykey, cat_str]
    csv.writer(g).writerow([storykey, cat_str])
      
    print 'total count: ' + str(tot_counter)    
    f.close()
    #g.close()
      
if __name__ == '__main__':    
    printCat('/home/ubuntu/newsright/halflifedata/story_category_run1.csv', '/home/ubuntu/newsright/categories_run1.csv', header=1)

