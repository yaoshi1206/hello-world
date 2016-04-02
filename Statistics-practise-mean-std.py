# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy

b=0
a=[0,]
print(len(a))
a[0]=float(input("Please input the number:"))
while (b!=-1): 
    print('You have iput',len(a),'number, ')    
    b=float(input("Please input the next number: "))
    if b!=-1:        
        a.append(b)
    else:
        pass
   
   
print("The results are:")
print("------------------output line-----------------------")
print("N=",len(a))
print("Max=",numpy.max(a))
print('Min=',numpy.min(a))
print('Mean=',numpy.mean(a))
print('STD=',numpy.std(a))
print('RSD=',numpy.std(a)/numpy.mean(a))

