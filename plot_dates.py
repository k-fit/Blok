import datetime
from matplotlib import pyplot as plt
from collections import Counter
from collections import OrderedDict

f = open('starbucks_times.csv', 'r')

dates = []
times = range(1,13) 
counts = 12 * [0]


for line in f:
    d = datetime.datetime.strptime(line.strip(), '%m/%d/%y %H:%M')
    dates.append(d) 

for d in dates:
    h = int( (d - dates[0]).total_seconds() / 3600 / 12)
    counts[h] += 1

print counts

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(times, counts, 'o-' )

y1, y2 = ax.get_ylim()
ax.set_ylim(0, 12)
ax.figure.canvas.draw()

x1, x2 = ax.get_xlim()
ax.set_xlim(1, 12)
ax.figure.canvas.draw()

plt.title('Publication Counts for the Starbucks/Square Phenomenon')
plt.xlabel('Half Days since first publication')
plt.ylabel('Number of Publications')

plt.savefig('starbucks_times.pdf')
