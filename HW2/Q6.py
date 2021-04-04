import matplotlib.pyplot as plt
import numpy as np
import csv

A1 = 0.997
A2 = 0.99
A3 = 0.9
A4 = 0.9985

B1 = 0.003
B2 = 0.01
B3 = 0.1
B4 = 0.0015
#fnew = 0
def IIRFilter(olist, nlist, start_index, A, B):
    
    new = olist[start_index - ii]

    new = A*new + B*olist[start_index]
    nlist.append(new)

def fft(t, data, nt, ndata, dt, A, B):

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
    ax1.set_title('A = ' + str(A) + ', ' + 'B = ' + str(B))
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

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t1.append(float(row[0])) # leftmost column
        data1.append(float(row[1])) # second column
dt1 = len(t1)/t1[-1]
ndata1 = []
new = data1[0]
for ii in range(1,len(data1)):
    new = A1*new + B1*data1[ii]
    ndata1.append(new)
print("Sample rate 1: " + str(dt1))
nt1 = t1[1:]
fft(t1, data1, nt1, ndata1, dt1, A1, B1)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t2.append(float(row[0])) # leftmost column
        data2.append(float(row[1])) # second column
dt2 = len(t2)/t2[-1]
ndata2 = []
new = data2[0]
for ii in range(1, len(data2)):
    new = A2*new + B2*data2[ii]
    ndata2.append(new)
print("Sample rate 2: " + str(dt2))
nt2 = t2[1:]
fft(t2, data2, nt2, ndata2, dt2, A2, B2)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t3.append(float(row[0])) # leftmost column
        data3.append(float(row[1])) # second column
dt3 = len(t3)/t3[-1]
ndata3 = []
new = data3[0]
for ii in range(1, len(data3)):
    new = A3*new + B3*data3[ii]
    ndata3.append(new)
print("Sample rate 3: " + str(dt3))
nt3 = t3[1:]
fft(t3, data3, nt3, ndata3, dt3, A3, B3)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t4.append(float(row[0])) # leftmost column
        data4.append(float(row[1])) # second column
dt4 = len(t4)/t4[-1]
ndata4 = []
new = data4[0]
for ii in range(1, len(data4)):
    new = A4*new + B4*data4[ii]
    ndata4.append(new)
print("Sample rate 4: " + str(dt4))
nt4 = t4[1:]
fft(t4, data4, nt4, ndata4, dt4, A4, B4)

plt.show()