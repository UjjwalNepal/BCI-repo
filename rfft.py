import numpy as np
import matplotlib.pyplot as plt
import csv
import scipy.fftpack
import itertools
#signal processing part
def fft(a):
	volt = 0.2197265625
	arr = volt*np.array(a)
	print('Brain Controlled Wheelchair')
	print('\n')
	plt.xlabel('Samples')
	plt.ylabel('Voltage')
	plt.plot(arr)
	plt.show()

	# Evaluating the FFT of the signal
	sp = scipy.fftpack.fft(arr,4096)
	N = len(sp)
	sp = sp[0:N/2]
	print(sp.round(3))
	plt.xlabel('Samples')
	plt.ylabel('Amplitude')
	plt.plot(sp)
	plt.show()
	# Calculating the real part and the imaginary part to calculate the magnitude
	x = sp.real
	y = sp.imag
	mag = []
	mag = x**2 + y**2
	#inst_power = mag
	#m  = mag**(1/2)
	print(mag)
	#print(m)
	lwave = 0
	j = 0
	k = 20
	l = 50
	n = 100
	#lower
	for i in mag:
		while(j<20):
				lwave += i
				j +=1
	lwave = (lwave*(10**(-12)))/20		
	print("The energy in lwave is",lwave)
	#from 20-50
	mwave = 0
	for i in mag[20:]:
		while(k<50):
				mwave += i
				k +=1	
	mwave = (mwave*(10**(-12)))/30
	print("The energy in mwave is",mwave)
	mhwave = 0
	for i in mag[50:]:
		while(l<100):
			mhwave += i
			l +=1
	mhwave = (mhwave*(10**(-12)))/50
	print("The energy in mhwave is",mhwave)
	hwave = 0
	for i in mag[100:]:
		while(n<512):
			hwave += i
			n +=1
	hwave = (hwave*(10**(-12)))/412		
	print("The energy in hwave is",hwave)
	#Plotting the magnitude spectrum
	lst = []
	lst.append(lwave)
	lst.append(mwave)
	lst.append(mhwave)
	lst.append(hwave)
	print('The maximum energy of the signal is at',max(lst))
	plt.xlabel('Samples')
	plt.ylabel('Power')
	plt.plot(mag)
	plt.show()

def main():
	data= []
	with open('i.csv','r')as f:
		reader = csv.reader(f)
		for i in reader:
			data.append(i)

	data = list(itertools.chain.from_iterable(data))
	split_list = []
	i = 0
	while i < len(data):
		broken_list = []
		broken_list = data[i:i+512]
		split_list.append(broken_list)
		i += 512
		if i >=512:
			break
	
	for i in range(10):
		split_list[i] = [int(j) for j in split_list[i]]
		print(split_list[i])
		fft(split_list[i])
		print('\n')


if __name__ == "__main__":main()
