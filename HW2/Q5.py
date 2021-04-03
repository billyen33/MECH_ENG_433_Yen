import matplotlib.pyplot as plt
import numpy as np
import statistics as stat
import csv

#list = [1,2,3,4,5,6,7,8]
#nlist = []
#x = 5
def AMFilter(olist, nlist, start_index, x):
    sum = 0
    for ii in range(x):
        sum = sum + olist[start_index+ii]
    nlist.append(sum/x)
    #print("nlist = "+ str(nlist[-1]))
#AMFilter(list,nlist, 1, x)

def fft(t, data, nt, ndata, dt):

    #dt = 1.0/10000.0 # 10kHz
    #t = np.arange(0.0, 1.0, dt) # 10s
    t = np.asarray(t)
    nt = np.asarray(nt)
    # a constant plus 100Hz and 1000Hz
    s = 4.0 * np.sin(2 * np.pi * 100 * t) + 0.25 * np.sin(2 * np.pi * 1000 * t) + 25

    Fs = dt # sample rate
    Ts = 1.0/Fs; # sampling interval
    ts = np.arange(0,t[-1],Ts) # time vector
    y = data # the data to make the fft from
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]

    #for the filtered data
    nts = np.arange(0,nt[-1],Ts) # time vector
    ny = ndata # the data to make the fft from
    nn = len(ny) # length of the signal
    nk = np.arange(nn)
    nT = nn/Fs
    nfrq = k/nT # two sides frequency range
    nfrq = nfrq[range(int(nn/2))] # one side frequency range
    nY = np.fft.fft(ny)/nn # fft computing and normalization
    nY = nY[range(int(nn/2))]

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.set_title(str(x) + ' Data Points Averaged')
    #ax1.plot(t,y,'b')
    #ax1.set_xlabel('Time')
    #ax1.set_ylabel('Amplitude')
    ax1.plot(t, data, 'black')
    ax1.plot(nt, ndata, 'red') #filtered
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Signal')
    ax2.loglog(frq,abs(Y),'black') # plotting the fft
    ax2.loglog(nfrq,abs(nY),'red') # plotting the filtered fft
    ax2.set_xlabel('Freq (Hz)')
    ax2.set_ylabel('|Y(freq)|')
    #plt.show()

t1 = []
t2 = []
t3 = []
t4 = []
data1 = [] # sigA
data2 = [] # sigB
data3 = [] # sigC
data4 = [] # sigD
x = 500
with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t1.append(float(row[0])) # leftmost column
        data1.append(float(row[1])) # second column
dt1 = len(t1)/t1[-1]
ndata1 = []
for ii in range(len(data1)-x):
    AMFilter(data1, ndata1, ii, x)
print("Sample rate 1: " + str(dt1))
nt1 = t1[0:-x]
fft(t1, data1, nt1, ndata1, dt1)
#fft(nt1, ndata1, dt1)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t2.append(float(row[0])) # leftmost column
        data2.append(float(row[1])) # second column
dt2 = len(t2)/t2[-1]
ndata2 = []
for ii in range(len(data2)-x):
    AMFilter(data2, ndata2, ii, x)
print("Sample rate 2: " + str(dt2))
nt2 = t2[0:-x]
fft(t2, data2, nt2, ndata2, dt2)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t3.append(float(row[0])) # leftmost column
        data3.append(float(row[1])) # second column
dt3 = len(t3)/t3[-1]
ndata3 = []
for ii in range(len(data3)-x):
    AMFilter(data3, ndata3, ii, x)
print("Sample rate 3: " + str(dt3))
nt3 = t3[0:-x]
fft(t3, data3, nt3, ndata3, dt3)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t4.append(float(row[0])) # leftmost column
        data4.append(float(row[1])) # second column
dt4 = len(t4)/t4[-1]
ndata4 = []
for ii in range(len(data4)-x):
    AMFilter(data4, ndata4, ii, x)
print("Sample rate 4: " + str(dt4))
nt4 = t4[0:-x]
fft(t4, data4, nt4, ndata4, dt4)

plt.show()