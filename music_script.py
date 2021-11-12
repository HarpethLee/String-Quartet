#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:40:47 2021

@author: johnlee
"""

##scaled beta
##Pareto

##superimposed normal distributions

## Imports
import threading
from pydub import AudioSegment
from pydub.playback import play
import numpy


## Import  violin wav files
vln_audio_1 = AudioSegment.from_file("Violin/violin_1.wav",
                               format="wav")

vln_audio_2 = AudioSegment.from_file("Violin/violin_2.wav",
                               format="wav")

vln_audio_3 = AudioSegment.from_file("Violin/violin_3.wav",
                               format="wav")

vln_audio_4 = AudioSegment.from_file("Violin/violin_4.wav",
                               format="wav")

vln_audio_5 = AudioSegment.from_file("Violin/violin_5.wav",
                               format="wav")

vln_audio_6 = AudioSegment.from_file("Violin/violin_6.wav",
                               format="wav")

vln_audio_7 = AudioSegment.from_file("Violin/violin_7.wav",
                               format="wav")

vln_audio_8 = AudioSegment.from_file("Violin/violin_8.wav",
                               format="wav")

## Import viola wav files
vla_audio_1 = AudioSegment.from_file("Viola/viola_1.wav",
                               format="wav")

vla_audio_2 = AudioSegment.from_file("Viola/viola_2.wav",
                               format="wav")

vla_audio_3 = AudioSegment.from_file("Viola/viola_3.wav",
                               format="wav")

vla_audio_4 = AudioSegment.from_file("Viola/viola_4.wav",
                               format="wav")

vla_audio_5 = AudioSegment.from_file("Viola/viola_5.wav",
                               format="wav")

vla_audio_6 = AudioSegment.from_file("Viola/viola_6.wav",
                               format="wav")

vla_audio_7 = AudioSegment.from_file("Viola/viola_7.wav",
                               format="wav")

vla_audio_8 = AudioSegment.from_file("Viola/viola_8.wav",
                               format="wav")

## Import cello wav files
c_audio_1 = AudioSegment.from_file("Cello/cello_1.wav",
                               format="wav")

c_audio_2 = AudioSegment.from_file("Cello/cello_2.wav",
                               format="wav")

c_audio_3 = AudioSegment.from_file("Cello/cello_3.wav",
                               format="wav")

c_audio_4 = AudioSegment.from_file("Cello/cello_4.wav",
                               format="wav")

c_audio_5 = AudioSegment.from_file("Cello/cello_5.wav",
                               format="wav")


## Import bass wav files
b_audio_1 = AudioSegment.from_file("Bass/bass_1.wav",
                             format = "wav")

b_audio_2 = AudioSegment.from_file("Bass/bass_2.wav",
                             format = "wav")

b_audio_3 = AudioSegment.from_file("Bass/bass_3.wav",
                             format = "wav")

b_audio_4 = AudioSegment.from_file("Bass/bass_4.wav",
                             format = "wav")

b_audio_5 = AudioSegment.from_file("Bass/bass_5.wav",
                             format = "wav")

b_audio_6 = AudioSegment.from_file("Bass/bass_6.wav",
                             format = "wav")


## Create violin functions
def vln_1():
    play(vln_audio_1)
    
def vln_2():
    play(vln_audio_2)
    
def vln_3():
    play(vln_audio_3)  

def vln_4():
    play(vln_audio_4)
    
def vln_5():
    play(vln_audio_5)
    
def vln_6():
    play(vln_audio_6)
    
def vln_7():
    play(vln_audio_7)
    
def vln_8():
    play(vln_audio_8)
    
    
## Create viola functions
def vla_1():
    play(vla_audio_1)
    
def vla_2():
    play(vla_audio_2)
    
def vla_3():
    play(vla_audio_3)
    
def vla_4():
    play(vla_audio_4)  

def vla_5():
    play(vla_audio_5)
    
def vla_6():
    play(vla_audio_6)
    
def vla_7():
    play(vla_audio_7)

def vla_8():
    play(vla_audio_8)
    
## Create cello functions
def c_1():
    play(c_audio_1)
    
def c_2():
    play(c_audio_2)
    
def c_3():
    play(c_audio_3)
    
def c_4():
    play(c_audio_4)
    
def c_5():
    play(c_audio_5)


## Create bass functions    
def b_1():
    play(b_audio_1)
    
def b_2():
    play(b_audio_2)
    
def b_3():
    play(b_audio_3)
    
def b_4():
    play(b_audio_4)
    
def b_5():
    play(b_audio_5)
    
def b_6():
    play(b_audio_6)
    


## Set play times
vln_t_1 = numpy.random.beta(2,8)

vln_t_2 = vln_t_1 + abs(numpy.random.normal(1.1, .25))

vla_t_1 = numpy.random.uniform(0,1.1)

vla_t_2 = vla_t_1 + numpy.random.exponential(0.85)

vla_t_3 = vla_t_2 + numpy.random.poisson(4)/(numpy.random.poisson(1)+1)
 
c_t_1 = numpy.random.uniform(.275,1.35)

c_t_2 = 2*c_t_1 + numpy.random.exponential(1.3)

c_t_3 = c_t_2 + abs(numpy.random.normal(0.1,2.5))

b_t_1 = vln_t_1 + 0.5

b_t_2 = b_t_1 + abs(numpy.random.normal(1.6, .5))

vln_t_3 = max(vln_t_2, vla_t_2) + 1.13

vln_t_4 = vln_t_3 + numpy.random.poisson(4)/(numpy.random.poisson(1)+1) + vln_audio_3.duration_seconds

vla_t_4 = vla_t_3 + 0.25 + numpy.random.poisson(3)/(numpy.random.poisson(1)+1)

vla_t_5 = vla_t_4 + abs(numpy.random.normal(0.1,2))

b_t_3 = vla_t_5 + 0.79

vln_t_5 = vln_t_4 + numpy.random.gamma(3,0.8)

c_t_4 = c_t_3 + c_audio_3.duration_seconds + numpy.random.poisson(2.5)

vla_t_6 = max(vla_t_5, vln_t_5) + numpy.random.uniform(0.5,5)

if b_t_3>vln_t_5:
   b_t_4 =  b_t_3 + b_audio_3.duration_seconds + numpy.random.uniform(0,0.5)
else:
    b_t_4 = vln_t_5 + numpy.random.exponential(2.1)
    
vln_t_6 = vln_t_5 + vln_audio_5.duration_seconds + numpy.random.exponential(2)

c_t_5 = c_t_4 + c_audio_4.duration_seconds + numpy.random.uniform()

b_t_5 = b_t_4 + b_audio_2.duration_seconds + abs(numpy.random.normal())

vla_t_7 = vla_t_6 + vla_audio_6.duration_seconds + abs(numpy.random.normal(0,2.2))

vla_t_8 = vla_t_7 + .5 + numpy.random.normal()**2

c_t_6 = c_t_5 + c_audio_5.duration_seconds + abs(numpy.random.normal(0,1.5))

vln_t_7 = vln_t_6 + numpy.random.gamma(2.1,1) + 0.1

vln_t_8 = max(vln_t_7,b_t_5) + abs(numpy.random.chisquare(.75))

vln_t_9 = vln_t_8 + numpy.random.poisson(1) + 1.13

c_t_7 = max(vln_t_8, c_t_6) + numpy.random.uniform(.2,1.6)

vln_t_10 = vln_t_9 + 2.613

vla_t_9 = max(vln_t_8, vla_t_8) + abs(numpy.random.normal(.5, 2))

vla_t_10 = vla_t_9 + abs(numpy.random.normal(2, .5))

b_t_6 = b_t_5 + b_audio_4.duration_seconds + numpy.random.exponential(.18) + .124

c_t_8 = c_t_7 + numpy.mean(numpy.random.exponential(3,2))

vla_t_11 = vla_t_10 + numpy.mean(numpy.random.exponential(2.8,2))

vln_t_11 = vln_t_10 + max(numpy.random.exponential(2.8,2))

vla_mod = numpy.random.uniform(.5,1)

vla_t_12 = vla_t_11 + 1.5*vla_mod

vla_t_13 = vla_t_12 + 1.6*vla_mod

vla_t_14 = vla_t_13 + 1.7*vla_mod

vla_t_15 = vla_t_14 + 1.8*vla_mod

c_t_9 = max(c_t_8, vln_t_11) + abs(numpy.random.normal(1,1.5))

c_t_10 = c_t_9 + c_audio_5.duration_seconds + numpy.random.uniform(2,5)

vla_t_16 = vla_t_15 + numpy.random.uniform(3,6)

vln_t_11 = vln_t_10 + numpy.random.uniform(2.5,5.5)

b_t_7 = b_t_6 + b_audio_5.duration_seconds + abs(numpy.random.normal(4,1))

vln_t_12 = max(vln_t_11, vla_t_16) + abs(numpy.random.normal(2,.5))
    
c_t_11 = c_t_10 + c_audio_5.duration_seconds + numpy.random.uniform(0,0.25)

vln_t_13 = vln_t_12 + vln_audio_6.duration_seconds + numpy.random.beta(2,8)

vln_t_14 = vln_t_13 + numpy.random.normal(1, .25) + .2

vla_t_17 = vla_t_16 + vla_audio_6.duration_seconds + numpy.random.uniform(0,1)

vla_t_18 = vla_t_17 + numpy.random.exponential(0.75)

vla_t_19 = vla_t_18 + numpy.random.poisson(4)/(numpy.random.poisson(1)+1)
 
c_t_12 = c_t_11 + c_audio_5.duration_seconds + numpy.random.uniform(.25,1.35)

c_t_13 = 2*c_t_2 + c_t_12 + numpy.random.exponential(1.2)

c_t_14 = c_t_13 + abs(numpy.random.normal(0,2.5))

b_t_8 = max(vln_t_12, b_t_7) + 0.5 + b_audio_2.duration_seconds

b_t_9 = b_t_8 + abs(numpy.random.normal(1.5, .5))

vln_t_15 = max(vln_t_14, vla_t_19) + 1.13

vln_t_16 = vln_t_15 + numpy.random.poisson(4)/(numpy.random.poisson(1)+1) + vln_audio_3.duration_seconds

vla_t_20 = vla_t_19 + 0.25 + numpy.random.poisson(3)/(numpy.random.poisson(1)+1)

vla_t_21 = vla_t_20 + abs(numpy.random.normal(0.2,2))

b_t_10 = vla_t_21 + 0.79

vln_t_17 = vln_t_16 + numpy.random.gamma(3,0.8)

c_t_15 = c_t_14 + c_audio_3.duration_seconds + numpy.random.poisson(2.5)

vla_t_22 = max(vla_t_21, vln_t_17) + numpy.random.uniform(0.5,5)

b_t_11 = b_t_10 + b_audio_3.duration_seconds + numpy.random.chisquare(3)

vla_t_23 = vla_t_22 + 1.5*(vla_mod + 0.5)

vla_t_24 = vla_t_23 + 1.6*vla_mod

vla_t_25 = vla_t_24 + 1.7*vla_mod

vla_t_26 = vla_t_25 + 1.8*vla_mod

c_t_16 = max(c_t_15, vln_t_17) + abs(numpy.random.normal(1.4,1.5))

c_t_17 = c_t_16 + c_audio_5.duration_seconds + numpy.random.uniform(2,5)

vla_t_27 = vla_t_26 + numpy.random.uniform(3,6)

vln_t_18 = vln_t_17 + numpy.random.uniform(2.5,5.5)

b_t_12 = b_t_11 + b_audio_5.duration_seconds + abs(numpy.random.normal(4,1))

vln_t_19 = max(vln_t_18, vla_t_27) + abs(numpy.random.normal(2,.5))
    
c_t_18 = c_t_17 + c_audio_5.duration_seconds + numpy.random.uniform(0,0.25)

vln_t_20 = vln_t_19 + vln_audio_6.duration_seconds + numpy.random.beta(2,8)

vln_t_21 = vln_t_20 + abs(numpy.random.normal(1, .25)) + .2

vla_t_28 = vla_t_27 + vla_audio_6.duration_seconds + numpy.random.uniform(0,1)

vla_t_29 = vla_t_28 + numpy.random.exponential(0.75)

vla_t_30 = vla_t_29 + numpy.random.poisson(4)/(numpy.random.poisson(1)+1)
 
c_t_19 = c_t_18 + c_audio_5.duration_seconds + numpy.random.uniform(.25,1.35)

c_t_20 = 2*c_t_2 + c_t_19 + numpy.random.exponential(1.2)

c_t_21 = c_t_20 + abs(numpy.random.normal(0.1,2.5))

b_t_13 = max(b_t_12, c_t_19) + b_audio_2.duration_seconds + numpy.random.exponential(1.75)

c_t_22 = max(c_t_21,b_t_13) + numpy.random.poisson(4)/(numpy.random.poisson(1)+1)

vla_t_31 = max(b_t_13, vla_t_30) + numpy.random.uniform(1.2, 3)

## Create timers
silence = AudioSegment.silent(duration=150000)

timer1 = threading.Timer(vln_t_1, vln_1)

quartet = silence.overlay(vln_audio_1, position=vln_t_1*1000)

timer2 = threading.Timer(vla_t_1, vla_1)

quartet = quartet.overlay(vla_audio_1, position = vla_t_1*1000)

timer3 = threading.Timer(c_t_1, c_1)

quartet = quartet.overlay(c_audio_1, position = c_t_1*1000)

timer4 = threading.Timer(b_t_1, b_1)

quartet = quartet.overlay(b_audio_1, position = b_t_1*1000)

timer5 = threading.Timer(vln_t_2, vln_2)

quartet = quartet.overlay(vln_audio_2, position = vln_t_2*1000)

timer6 = threading.Timer(vla_t_2, vla_2)

quartet = quartet.overlay(vla_audio_2, position = vla_t_2*1000)

timer7 = threading.Timer(vln_t_3, vln_3)

quartet = quartet.overlay(vln_audio_3, position = vln_t_3*1000)

timer8 = threading.Timer(b_t_2, b_2)

quartet = quartet.overlay(b_audio_2, position = b_t_2*1000)

timer9 = threading.Timer(c_t_2, c_2)

quartet = quartet.overlay(c_audio_2, position = c_t_2*1000)

timer10 = threading.Timer(vln_t_4, vln_4)

quartet = quartet.overlay(vln_audio_4, position = vln_t_4*1000)

timer11 = threading.Timer(vla_t_3, vla_3)

quartet = quartet.overlay(vla_audio_3, position = vla_t_3*1000)

timer12 = threading.Timer(vla_t_4, vla_4)

quartet = quartet.overlay(vla_audio_4, position = vla_t_4*1000)

timer13 = threading.Timer(vla_t_5, vla_5)

quartet = quartet.overlay(vla_audio_5, position = vla_t_5*1000)

timer14 = threading.Timer(b_t_3, b_3)

quartet = quartet.overlay(b_audio_3, position = b_t_3*1000)

timer15 = threading.Timer(c_t_3, c_3)

quartet = quartet.overlay(c_audio_3, position = c_t_3*1000)

timer16 = threading.Timer(vln_t_5, vln_5)

quartet = quartet.overlay(vln_audio_5, position = vln_t_5*1000)

timer17 = threading.Timer(c_t_4, c_4)

quartet = quartet.overlay(c_audio_4, position = c_t_4*1000)

timer18 = threading.Timer(vla_t_6, vla_6)

quartet = quartet.overlay(vla_audio_6, position = vla_t_6*1000)

timer19 = threading.Timer(b_t_4, b_2)

quartet = quartet.overlay(b_audio_2, position = b_t_4*1000)

ind_1 = numpy.random.randint(1,4)
if ind_1 == 1:
    timer20 = threading.Timer(vln_t_6, vln_1)
    quartet = quartet.overlay(vln_audio_1, position = vln_t_6*1000)
if ind_1 == 2:
    timer20 = threading.Timer(vln_t_6, vln_2)
    quartet = quartet.overlay(vln_audio_2, position = vln_t_6*1000)
else:
    timer20 = threading.Timer(vln_t_6, vln_3)
    quartet = quartet.overlay(vln_audio_3, position = vln_t_6*1000)
    
timer21 = threading.Timer(c_t_5, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_5*1000)

timer22 = threading.Timer(b_t_5, b_4)

quartet = quartet.overlay(b_audio_4, position = b_t_5*1000)

timer23 = threading.Timer(vla_t_7, vla_3)

quartet = quartet.overlay(vla_audio_3, position = vla_t_7*1000)

timer24 = threading.Timer(vla_t_8, vla_7)

quartet = quartet.overlay(vla_audio_7, position = vla_t_8*1000)

timer25 = threading.Timer(c_t_6, c_2)

quartet = quartet.overlay(c_audio_2, position = c_t_6*1000)

timer26 = threading.Timer(vln_t_7, vln_6)

quartet = quartet.overlay(vln_audio_6, position = vln_t_7*1000)

ind_2 = numpy.random.randint(1,4)
if ind_2 ==1:
    timer27 = threading.Timer(vln_t_8, vln_6)
    quartet = quartet.overlay(vln_audio_6, position = vln_t_8*1000)
if ind_2 ==2:
    timer27 = threading.Timer(vln_t_8, vln_7)
    quartet = quartet.overlay(vln_audio_7, position = vln_t_8*1000)
else:
    timer27 = threading.Timer(vln_t_8, vln_8)
    quartet = quartet.overlay(vln_audio_8, position = vln_t_8*1000)

    
if ind_1 ==1:
    timer28 = threading.Timer(vln_t_9, vln_6)
    quartet = quartet.overlay(vln_audio_6, position = vln_t_9*1000)
if ind_1 ==2:
    timer28 = threading.Timer(vln_t_9, vln_7)
    quartet = quartet.overlay(vln_audio_7, position = vln_t_9*1000)
else:
    timer28 = threading.Timer(vln_t_9, vln_8)
    quartet = quartet.overlay(vln_audio_8, position = vln_t_9*1000)

    
timer29 = threading.Timer(c_t_7, c_1)

quartet = quartet.overlay(c_audio_1, position = c_t_7*1000)

if ind_1 ==1:
    timer30 = threading.Timer(vln_t_10, vln_8)
    quartet = quartet.overlay(vln_audio_8, position = vln_t_10*1000)
if ind_1 ==2:
    timer30 = threading.Timer(vln_t_10, vln_7)
    quartet = quartet.overlay(vln_audio_7, position = vln_t_10*1000)
else:
    timer30 = threading.Timer(vln_t_10, vln_6)
    quartet = quartet.overlay(vln_audio_6, position = vln_t_10*1000)

    
timer31 = threading.Timer(vla_t_9, vla_2)

quartet = quartet.overlay(vla_audio_2, position = vla_t_9*1000)

timer32 = threading.Timer(vla_t_10, vla_4)

quartet = quartet.overlay(vla_audio_4, position = vla_t_10*1000)

timer33 = threading.Timer(b_t_6, b_5)

quartet = quartet.overlay(b_audio_5, position = b_t_6*1000)

timer34 = threading.Timer(c_t_8, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_8*1000)

timer35 = threading.Timer(vla_t_11, vla_5)

quartet = quartet.overlay(vla_audio_5, position = vla_t_11*1000)

timer36 = threading.Timer(vln_t_11, vln_5)

quartet = quartet.overlay(vln_audio_5, position = vln_t_11*1000)

timer37 = threading.Timer(vla_t_12, vla_4)

quartet = quartet.overlay(vla_audio_4, position = vla_t_12*1000)

timer38 = threading.Timer(vla_t_13, vla_3)

quartet = quartet.overlay(vla_audio_3, position = vla_t_13*1000)

timer39 = threading.Timer(vla_t_14, vla_2)

quartet = quartet.overlay(vla_audio_2, position = vla_t_14*1000)

timer40 = threading.Timer(vla_t_15, vla_1)

quartet = quartet.overlay(vla_audio_1, position = vla_t_15*1000)

timer41 = threading.Timer(c_t_9, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_9*1000)

timer42 = threading.Timer(c_t_10, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_10*1000)

timer43 = threading.Timer(vln_t_11, vln_7)

quartet = quartet.overlay(vln_audio_7, position = vln_t_11*1000)

timer44 = threading.Timer(vla_t_16, vla_6)

quartet = quartet.overlay(vla_audio_6, position = vla_t_16*1000)

timer45 = threading.Timer(b_t_7, b_2)

quartet = quartet.overlay(b_audio_2, position = b_t_7*1000)

timer46 = threading.Timer(vln_t_12, vln_6)

quartet = quartet.overlay(vln_audio_6, position = vln_t_12*1000)

timer47 = threading.Timer(c_t_11, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_11*1000)

timer48 = threading.Timer(vln_t_13, vln_1)

quartet = quartet.overlay(vln_audio_1, position = vln_t_13*1000)

timer49 = threading.Timer(vla_t_17, vla_1)

quartet = quartet.overlay(vla_audio_1, position = vla_t_17*1000)

timer50 = threading.Timer(c_t_12, c_1)

quartet = quartet.overlay(c_audio_1, position = c_t_12*1000)

timer51 = threading.Timer(b_t_8, b_1)

quartet = quartet.overlay(b_audio_1, position = b_t_8*1000)

timer52 = threading.Timer(vln_t_14, vln_2)

quartet = quartet.overlay(vln_audio_2, position = vln_t_14*1000)

timer53 = threading.Timer(vla_t_18, vla_2)

quartet = quartet.overlay(vla_audio_2, position = vla_t_18*1000)

timer54 = threading.Timer(vln_t_15, vln_3)

quartet = quartet.overlay(vln_audio_3, position = vln_t_15*1000)

timer55 = threading.Timer(b_t_9, b_2)

quartet = quartet.overlay(b_audio_2, position = b_t_9*1000)

timer56 = threading.Timer(c_t_13, c_2)

quartet = quartet.overlay(c_audio_2, position = c_t_13*1000)

timer57 = threading.Timer(vln_t_16, vln_4)

quartet = quartet.overlay(vln_audio_4, position = vln_t_16*1000)

timer58 = threading.Timer(vla_t_19, vla_3)

quartet = quartet.overlay(vla_audio_3, position = vla_t_19*1000)

timer59 = threading.Timer(vla_t_20, vla_4)

quartet = quartet.overlay(vla_audio_4, position = vla_t_20*1000)

timer60 = threading.Timer(vla_t_21, vla_5)

quartet = quartet.overlay(vla_audio_5, position = vla_t_21*1000)

timer61 = threading.Timer(b_t_10, b_3)

quartet = quartet.overlay(b_audio_3, position = b_t_10*1000)

timer62 = threading.Timer(c_t_14, c_3)

quartet = quartet.overlay(c_audio_3, position = c_t_14*1000)

timer63 = threading.Timer(vln_t_17, vln_5)

quartet = quartet.overlay(vln_audio_5, position = vln_t_17*1000)

timer64 = threading.Timer(c_t_15, c_4)

quartet = quartet.overlay(c_audio_4, position = c_t_15*1000)

timer65 = threading.Timer(vla_t_22, vla_6)

quartet = quartet.overlay(vla_audio_6, position = vla_t_22*1000)

timer66 = threading.Timer(b_t_11, b_6)

quartet = quartet.overlay(b_audio_6, position = b_t_11*1000)

timer67 = threading.Timer(vla_t_23, vla_4)

quartet = quartet.overlay(vla_audio_4, position = vla_t_23*1000)

timer68 = threading.Timer(vla_t_24, vla_3)

quartet = quartet.overlay(vla_audio_3, position = vla_t_23*1000)

timer69 = threading.Timer(vla_t_25, vla_2)

quartet = quartet.overlay(vla_audio_2, position = vla_t_25*1000)

timer70 = threading.Timer(vla_t_26, vla_1)

quartet = quartet.overlay(vla_audio_1, position = vla_t_26*1000)

timer71 = threading.Timer(c_t_16, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_16*1000)

timer72 = threading.Timer(c_t_17, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_17*1000)

timer73 = threading.Timer(vln_t_18, vln_7)

quartet = quartet.overlay(vln_audio_7, position = vln_t_18*1000)

timer74 = threading.Timer(vla_t_27, vla_6)

quartet = quartet.overlay(vla_audio_6, position = vla_t_27*1000)

timer75 = threading.Timer(b_t_12, b_2)

quartet = quartet.overlay(b_audio_2, position = b_t_12*1000)

timer76 = threading.Timer(vln_t_19, vln_6)

quartet = quartet.overlay(vln_audio_6, position = vln_t_19*1000)

timer77 = threading.Timer(c_t_18, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_18*1000)

timer78 = threading.Timer(vln_t_20, vln_1)

quartet = quartet.overlay(vln_audio_1, position = vln_t_20*1000)

timer79 = threading.Timer(vla_t_28, vla_1)

quartet = quartet.overlay(vla_audio_1, position = vla_t_28*1000)

timer80 = threading.Timer(c_t_19, c_1)

quartet = quartet.overlay(c_audio_1, position = c_t_19*1000)

timer81 = threading.Timer(c_t_20, c_2)

quartet = quartet.overlay(c_audio_2, position = c_t_20*1000)

timer82 = threading.Timer(c_t_21, c_2)

quartet = quartet.overlay(c_audio_2, position = c_t_21*1000)

timer83 = threading.Timer(b_t_13, b_4)

quartet = quartet.overlay(b_audio_4, position = b_t_13*1000)

timer84 = threading.Timer(c_t_22, c_5)

quartet = quartet.overlay(c_audio_5, position = c_t_22*1000)

timer85 = threading.Timer(vla_t_29, vla_2)

quartet = quartet.overlay(vla_audio_2, position = vla_t_29*1000)

timer86 = threading.Timer(vla_t_30, vla_2)

quartet = quartet.overlay(vla_audio_2, position = vla_t_30*1000)

timer87 = threading.Timer(vla_t_31, vla_8)

quartet = quartet.overlay(vla_audio_8, position = vla_t_31*1000)

timer88 = threading.Timer(c_t_20, vln_7)

quartet = quartet.overlay(vln_audio_7, position = c_t_20*1000)

timer89 = threading.Timer(c_t_22, vln_6)

quartet = quartet.overlay(vln_audio_6, position = c_t_22*1000)

timer90 = threading.Timer(c_t_22 + 2, vln_8)

quartet = quartet.overlay(vln_audio_8, position = c_t_22*1000)

timer91 = threading.Timer(b_t_13 + 6, b_1)

quartet = quartet.overlay(b_audio_1, position = b_t_13*1000)
   
quartet.export("quartet3.wav", format = "wav")

exit()

## Start Timers
timer1.start()

timer2.start()

timer3.start()

timer4.start()

timer5.start()

timer6.start()

timer7.start()

timer8.start()

timer9.start()

timer10.start()

timer11.start()

timer12.start()

timer13.start()

timer14.start()

timer15.start()

timer16.start()

timer17.start()

timer18.start()

timer19.start()

timer20.start()

timer21.start()

timer22.start()

timer23.start()

timer24.start()

timer25.start()

timer26.start()

timer27.start()

timer28.start()

timer29.start()

timer30.start()

timer31.start()

timer32.start()

timer33.start()

timer34.start()

timer35.start()

timer36.start()

timer37.start()

timer38.start()

timer39.start()

timer40.start()

timer41.start()

timer42.start()

timer43.start()

timer44.start()

timer45.start()

timer46.start()

timer47.start()

timer48.start()

timer49.start()

timer50.start()

timer51.start()

timer52.start()

timer53.start()

timer54.start()

timer55.start()

timer56.start()

timer57.start()

timer58.start()

timer59.start()

timer60.start()

timer61.start()

timer62.start()

timer63.start()

timer64.start()

timer65.start()

timer66.start()

timer67.start()

timer68.start()

timer69.start()

timer70.start()

timer71.start()

timer72.start()

timer73.start()

timer74.start()

timer75.start()

timer76.start()

timer77.start()

timer78.start()

timer79.start()

timer80.start()

timer81.start()

timer82.start()

timer83.start()

timer84.start()

timer85.start()

timer86.start()

timer87.start()

timer88.start()

timer89.start()

timer90.start()

timer91.start()