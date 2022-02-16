# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:49:23 2021

@author: Uğur Levent Akaoğlu
2284099
"""
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np


class image:
    
    def __init__(self,nrow,ncol):
        self.nrow=nrow
        self.ncol=ncol
        self.arr=np.zeros((nrow+1,ncol+1),dtype='i,i,i')
        #print(self.arr)
    
    def addColor(self,row,col,value):
        value= list(value.itertuples(index=False, name=None))
        #print(value)
        self.arr[row,col]= value
        
    
    def randomizeImage(self):
        for i in range(len(self.arr[:,0])):
            for j in range(len(self.arr[0,:])):
                self.arr[i,j]=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        
    def showImage(self):
        showit=self.arr.tolist()
        plt.imshow(showit)
        
    
   
    
   
    
df= pd.read_csv('example_image.txt')
df.columns=['A','B','C','D','E']

img= image(df.loc[df.index[-1],'A'],df.loc[df.index[-1],'B'])

row=df['A']
column=df['B']
df=df.drop(['A','B'],axis=1)


img.addColor(row,column,df) 
img.showImage()
#img.randomizeImage()
img.showImage()