__author__ = 'Brendan'

# lake culture data from city of chicago


import csv
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

cultureDataPath = 'C:\Users\Brendan\Downloads\Beach_Lab_Data.csv'
f = open(cultureDataPath)
csv_f = csv.reader(f)

allBeachEntries = [];
for row in csv_f:
    allBeachEntries.append(row[2])

# get the list of unique beaches
uniqueBeachEntries = np.unique(allBeachEntries)
print uniqueBeachEntries
numBeaches = len(uniqueBeachEntries)
for beach in uniqueBeachEntries:
    print beach


y_57thSt = [];
t_57thSt = [];
f.seek(0) # reset the file so csv reader can see the rows again, '%Y-%m-%d %H:%M:%S'
numEntries = 0
for row in csv_f:
    if row[2] == '57th Street':
        if row[3] != '': # some days are missing data
            y_57thSt.append(row[3])
            timestamp = datetime.datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p'); # interpret as a timestamp
            t_entry = timestamp # wonder how best to represent time
            print t_entry
            t_57thSt.append(t_entry)
            numEntries += 1
print y_57thSt
print t_57thSt

# sort the list of times because they're out of order for some reason
sorted_t_idx_list = sorted(range(len(t_57thSt)),key=lambda x:t_57thSt[x])
Ts = [t_57thSt[i] for i in sorted_t_idx_list ]
Ys = [y_57thSt[i] for i in sorted_t_idx_list ]
# sort the list of readings too of course


# population timeseries for individual beaches



# plot
# try plot just 57th st

plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.plot(Ts, Ys)
plt.gcf().autofmt_xdate()
plt.show()
'''
plt.figure()
xx = range(0,numEntries,1)
yy = y_57thSt
plt.scatter(xx,yy)
plt.show()
'''
plt.figure()
yy = range(0,numEntries,1)
xx = Ts
#plt.plot_datetime(xx,yy)
#plt.show()


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.plot(xx,yy)
plt.gcf().autofmt_xdate()

plt.show()