#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 13:03:56 2018

@author: wzb
"""
import time
import numpy as np
#np.random.seed(500)
def intial_numbers(n):
    ori_a=np.random.randint(0,10,n)
    ori_a=np.append(ori_a,np.random.randint(-1,1,1))
    ori_b=np.random.randint(0,10,n)
    ori_b=np.append(ori_b,np.random.randint(-1,1,1))
    return ori_a,ori_b

def recover_function(ori_a):
    if ori_a[-1]==0:
        num=''
    else:
        num='-'
    for i in -np.sort(-np.arange(len(ori_a)-1)):
        num+=str(ori_a[i])
    return num

def sub_minus_function(ori_a,ori_b):
    if len(ori_a)==len(ori_b):
        for i in -np.sort(-np.arange(len(ori_a)-1)):
            d=ori_a[i]-ori_b[i]
            if d!=0:
                break
        if d<0:
            d=sub_minus_function(ori_b,ori_a)
            d[-1]=-1
            return d
    if len(ori_a)<len(ori_b):
        d=sub_minus_function(ori_b,ori_a)
        d[-1]=-1
        return d
    else:
        c=np.zeros(len(ori_a),dtype=int)
        for i in np.arange(len(ori_b)-1):
            d=c[i]+ori_a[i]-ori_b[i]
            if d>=0:
                c[i]=d
            else:
                c[i+1]-=1
                c[i]=d+10
        while len(c)>0 and c[-1]==0:
            c=np.delete(c,-1)
        if len(c)==0:
            c=np.array([0])
        else:
            c=np.append(c,0)
        return c
    
        

def minus_function(ori_a,ori_b):
    if ori_b[-1]==0:
        ori_b[-1]=-1
    else:
        ori_b[-1]=0
    if ori_a[-1]==ori_b[-1]:
        return plus_function(ori_a,ori_b)
    else:   
        if ori_a[-1]==0:
            c=sub_minus_function(ori_a,ori_b)
            return c
        else:
            c=sub_minus_function(ori_b,ori_a)
            return c

def plus_function(ori_a,ori_b):
    c=np.zeros(np.maximum(len(ori_a),len(ori_b))+1,dtype=int)
    if ori_a[-1]!=ori_b[-1]:
        if ori_b[-1]==0:
            return sub_minus_function(ori_b,ori_a)
        else:
            return sub_minus_function(ori_a,ori_b)
    else:
        for i in range(np.minimum(len(ori_a),len(ori_b))-1):
            d=ori_a[i]+ori_b[i]+c[i]
            if d>9:
                d-=10
                c[i]=d
                c[i+1]+=1
            else:
                c[i]=d
        if c[len(c)-2]!=0:
            c[-1]=ori_a[-1]
        else:
            c=np.delete(c,-1)
            c[-1]=ori_a[-1]
        return c
    
def div_function(ori_a,ori_b):
    if np.max(ori_b)!=0:
        first_part=[0]*(len(ori_a)//len(ori_b)+1)
        sign=0
        if ori_a[-1]==ori_b[-1]:
            sign=''
        else:
            sign='-'
        ori_a[-1]=0
        ori_b[-1]=0
        c=ori_a.copy()
        while len(c)>1:
            c=sub_minus_function(c,ori_b)
            c_last=c.copy()
            if c[-1]==0 and len(c)!=1:
               first_part[0]+=1
               for i in range(len(first_part)-1):
                   if first_part[i]>10:
                       first_part[i]-=10
                       first_part[i+1]+=1
            elif len(c)==1:
                second_part=np.array([0,0])
            else:
                if sign=='-':
                    first_part[0]+=1
                    c[-1]=0
                    second_part=c
                else:
                    second_part=c_last   
                break
        return sign+recover_function(first_part)+'+'+recover_function(second_part)
    else:
        return 'impossible'
        
def mutlipy_function(ori_a,ori_b):
    if ori_a[-1]==ori_b[-1]:
        sign=0
    else:
        sign=-1
    c=np.zeros(len(ori_a)+len(ori_b)-2,dtype=int) 
    for i in range(len(ori_a)-1):
        for j in range(len(ori_b)-1):
            d=ori_a[i]*ori_b[j]
            c[i+j]+=d
            k=0
            while True:
                if c[i+j+k]>9:
                    c[i+j+k+1]+=1
                    c[i+j+k]-=10
                else: 
                    k+=1
                    if i+j+k==len(ori_a)+len(ori_b)-2:
                        break
    while c[-1]==0:
        c=np.delete(c,-1)
        if len(c)==0:
            c=np.array([0])
            break
    if c[-1]!=0:
        c=np.append(c,sign)
    return c
                
def whole_process(n,times):
    for i in range(times):
        a,b=intial_numbers(n)
        print('time:',i+1)
        print('the ori_a is:',a)
        print('the ori_b is:',b)
        plus=recover_function(plus_function(a.copy(),b.copy()))
        print('plus is:',plus)
        minus=recover_function(minus_function(a.copy(),b.copy()))
        print('minus is:',minus)
        dive=div_function(a.copy(),b.copy())
        print('div is:',dive)
        mutlipy=recover_function(mutlipy_function(a.copy(),b.copy()))
        print('mutlipy is:',mutlipy)
        
if __name__ == "__main__":
    n=4
    times=1000
    start=time.time()
    whole_process(n,times)
    end = time.time()
    print(n)
    print(times)
    print(end-start)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    