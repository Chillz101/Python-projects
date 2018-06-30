# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:52:06 2018

@author: malti
"""

#music notic is a collecion of fundamental tones and harmonics or overtones.
import numpy as np
import soundfile as sf
import sounddevice as sd


amp = [1,1]
amp_a = [[1,0,0,0],[1,1/2,1/3,1/4]]
freq = [1000,440]




def tone(duration = 1,freq = 1000,amp = 1, sample_rate=20000,rtimes = False):
    ''' This function genarates tones 
         With no parameter it generates an array representing a 1kHz tone'''
    times = np.linspace(0,duration,sample_rate * duration) #
    #short_clip = np.zeros(sample_rate * time - 1)
    overtone = np.cos(2 * np.pi * freq * times) * amp
    if rtimes == True:
        return overtone , times
    elif rtimes == False:
        return overtone
    else:
        print('error in parameters')
    

# tone synthesis
def note(freq, lent, amp=1, rate=20000):
 t = np.linspace(0,lent,lent*rate)
 data = np.cos(2*np.pi*freq*t)*amp
 return data.astype('int16') # two byte integers

def complex_tone(freq,amp_array,duration = 0.5,rate = 20000):
    data = np.zeros(np.size(rate * duration))
    for i , n in enumerate(amp_array):
        data = data + tone(duration,freq = (i+1) * freq ,amp = n,sample_rate = rate)
    return data

def complex_sound(freq_array,amp_array,duration,rate = 20000):
    if len(amp_array) != len(freq_array):
        return None
    data = np.zeros(np.size(rate * duration))
    for index_freq , n_freq in enumerate(freq_array):
        
        for index_amp , n_amp in enumerate(amp_array[index_freq]):
            data = data + tone(duration,freq = (index_freq+1) * n_freq ,amp = n_amp,sample_rate = rate)
    return data

def blank_sound(duration,rate = 20000):
    data = np.zeros(np.size(rate * duration))
    return data


def tick1(d,f,p,n):
    for i in range(0,n):
        sd.play(tone(d,f,2))
        sd.play(blank_sound(d))
        

def tick(d,f,p,n):
    for i in p:
        if i > 0:
            j = 0
            for j in range(0,i):
                sd.play(tone(d,f,2))
                sd.wait()
                #sd.play(blank_sound(d))
        else:
                sd.play(blank_sound(1))  
                
# A tone, 2 seconds, 44100 samples per second
#tonep = note(440,2,amp=1)
#tonex = tone(duration = 2,freq = 440,amp = 1)
