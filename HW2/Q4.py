import matplotlib.pyplot as plt
import numpy as np
import csv

def fft(t, data, dt):

    #dt = 1.0/10000.0 # 10kHz
    #t = np.arange(0.0, 1.0, dt) # 10s
    t = np.asarray(t)
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

    fig, (ax1, ax2) = plt.subplots(2, 1)
    #ax1.plot(t,y,'b')
    #ax1.set_xlabel('Time')
    #ax1.set_ylabel('Amplitude')
    ax1.plot(t, data)
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Signal')
    ax2.loglog(frq,abs(Y),'b') # plotting the fft
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

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t1.append(float(row[0])) # leftmost column
        data1.append(float(row[1])) # second column
dt1 = len(t1)/t1[-1]
print("Sample rate 1: " + str(dt1))
fft(t1, data1, dt1)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t2.append(float(row[0])) # leftmost column
        data2.append(float(row[1])) # second column
dt2 = len(t2)/t2[-1]
print("Sample rate 2: " + str(dt2))
fft(t2, data2, dt2)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t3.append(float(row[0])) # leftmost column
        data3.append(float(row[1])) # second column
dt3 = len(t3)/t3[-1]
print("Sample rate: " + str(dt3))
fft(t3, data3, dt3)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t4.append(float(row[0])) # leftmost column
        data4.append(float(row[1])) # second column
dt4 = len(t4)/t4[-1]
print("Sample rate: " + str(dt4))
fft(t4, data4, dt4)

plt.show()