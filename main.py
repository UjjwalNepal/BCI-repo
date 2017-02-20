# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:29:04 2016

@author: ujjwal
"""

import mindwave,time, csv
from espeak import espeak
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import sys
import socket
import threading
import Queue

queue = Queue.Queue()
state = 'A'
output = False
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.0.100", 5002))
    
def Func():
    data_buffer = []
    while True:
        def fft(a):
            global state
            global output
            volt = 0.2197265625
            arr = volt*np.array(a)
            #print('FFT Samples')
            #print('\n')
            
            # Evaluating the FFT of the signal
            sp = scipy.fftpack.fft(arr)
            sp = sp[1:100]
            #print(sp)
            #print('\n')
            
            
            # Calculating the real part and the imaginary part to calculate the magnitude
            x = sp.real
            y = sp.imag

            m = []
            m = x**2 + y**2
            
            #print('Magnitude values')
            #print(m)
            print('\n')
            #Power in Delta_Theta Band
            theta = 0
            delta = 0
            alpha = 0
            beta = 0
            gamma = 0
            
            for i in m[1:4]:
                delta += i
            delta = (delta*(10**(-5)))/3		# Actually have to be multiplied by 10^-12
            #print("The power in Delta is",delta)
            
            for i in m[4:8]:
                theta += i
            theta = (theta*(10**(-5)))/4		# Actually have to be multiplied by 10^-12
            #print("The power in Theta is",theta)
            
            # Power in alpha Band.
            for i in m[8:13]:
                alpha += i
            alpha = (alpha*(10**(-5)))/5
            print("The power in alpha band is",alpha)
            
            # Power in  beta Band.
            for i in m[13:41]:
                beta += i
            beta = (beta*(10**(-5)))/28
            print("The power in beta is",beta)
            
            if alpha >= 4:
                alpha = 1
            else:
                alpha = 0
            
            
                    
            
            # Power in gamma Band.
            for i in m[41:100]:
                gamma += i		
            gamma = ((gamma- m[50])*(10**(-5)))/58	
            #print("The power in gamma band is",gamma)
            
            if state == 'A':
                if alpha == 1:
                    state = 'B'
                else:
                    state = 'D'
            elif state == 'B':
                if alpha == 1:
                    state = 'C'
                else:
                    state = 'D'
            elif state == 'C':
                if alpha == 1:
                    state = 'E'
                    output = False
                else:
                    state = 'D'
            elif state == 'D':
                if alpha == 1:
                    state = 'B'
                else:
                    state = 'F'
            elif state == 'E':
                if alpha == 1:
                    state = 'E'
                    output = False
                else:
                    state = 'D'
            elif state == 'F':
                if alpha == 1:
                    state = 'B'
                else:
                    state = 'G'
                    output = True
            elif state == 'G':
                if alpha == 1:
                    state = 'B'
                else:
                    state = 'G'
                    output = True
            else:
                state = 'A'
            print(output)
            if output == True:
                
                client_socket.send('1')
            else:
                espeak.synth("Wheelchair is not moving")
                client_socket.send('0')
          
        data=queue.get()
        data_buffer.append(data)
        if len(data_buffer) == 512:
            #print('Time Series Data',data_buffer)
            #print('-----------------------------------------')
            #print('\n')
            fft(data_buffer)
            data_buffer = []
    
def MainThread():
    while True:
        
        def on_raw(headset,raw):
            queue.put(raw)
            #print queue.get()
            data = []
            data.append(raw)
            path = "relaxy.csv"
            printraw(data,path)
        def printraw(data,path):
            with open(path,'a') as f:
                writer = csv.writer(f)
                for i in data:
                    writer.writerow(data)
								
        headset = mindwave.Headset('/dev/ttyUSB0')
        time.sleep(1)
    
        headset.connect()
        print("Connecting")
    
        while headset.status != 'connected':
            time.sleep(0.5)
            if headset.status == 'standby':
                headset.connect()
                print("Retrying")
        try:
        	print("connected")
        	
        	
        	headset.raw_value_handlers.append(on_raw)
        	time.sleep(1200)
        	headset.disconnect()
        except KeyboardInterrupt:
            headset.disconnect()
        except:
            headset.disconnect()
            print("Unknown Error")
            raise
            
if __name__ == '__main__':
    try:        
        tm = threading.Thread(name="project",target=MainThread)
        tm.start()
        time.sleep(1)
        t1 = threading.Thread(name="func", target=Func)
        t1.start()
        t1.join()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
        
        
        
        
