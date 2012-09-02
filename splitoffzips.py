def splitoffzips(fileaddition):
    f = open('/home/ubuntu/newsright/halflifedata/half_life_%s.txt' % (fileaddition), 'r')
    halflife = open('/home/ubuntu/newsright/halflifedata/halflifeinfo_%s.txt' % (fileaddition), 'w')
    zips = open('/home/ubuntu/newsright/halflifedata/zips_%s.txt' % (fileaddition), 'w')

    for line in f:
        values = line.strip().split(',')
        halflife.write(','.join(values[0:3]) + '\n')
        zipcodes = values[3].split('#')
        for zipcode in zipcodes:
            zips.write(values[0] + ',' + zipcode + '\n')

if __name__ == '__main__':
    splitoffzips('run1')
