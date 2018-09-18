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
        num='+'
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
        for i in sorted(range(len(ori_a)-1),reverse=True):
            if ori_a[i]!=0:
                break
        for j in sorted(range(len(ori_b)-1),reverse=True):
            if ori_b[i]!=0:
                break
        first_part=[0]*max(0,i-j)+[0]
        sign=0
        if ori_a[-1]==ori_b[-1]:
            sign=''
        else:
            sign='-'
        ori_a[-1]=0
        ori_b[-1]=0
        c=ori_a.copy()
        while len(c)>1:
            c_last=c.copy()
            c=sub_minus_function(c,ori_b)
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
                    c_last[-1]=0
                    second_part=c_last
                break
        first_part.append(0)
        return sign+recover_function(first_part)[1:]+recover_function(second_part)
    else:
        return 'impossible'

def new_div_function(a,b):
    ori_a=a.copy()
    ori_b=b.copy()
    if np.max(ori_b)!=0:
        for i in sorted(range(len(ori_a)-1),reverse=True):
            if ori_a[i]!=0:
                break
        for j in sorted(range(len(ori_b)-1),reverse=True):
            if ori_b[i]!=0:
                break
        first_part=[0]*max(0,i-j)+[0]
        sign=0
        if ori_a[-1]==ori_b[-1]:
            sign='+'
        else:
            sign='-'
        ori_a[-1]=0
        ori_b[-1]=0
        c=ori_a.copy()
        for i in sorted(range(len(first_part)),reverse=True):
            mutilpy_num=[0]*(i)+[1]+[0]
            if i!=0:
                con=True
                while con:
                    divden_num=mutlipy_function(mutilpy_num,ori_b)
                    diff_digits=len(c)-len(divden_num)
                    if diff_digits>=0:
                        divden_num=np.append(divden_num,np.repeat(0,diff_digits))
                    else:
                        divden_num=np.append(c,np.repeat(0,-diff_digits))
                    d=sub_minus_function(c,divden_num)
                    if d[-1]==0:
                        first_part[i]+=1
                        c=d.copy()
                    else:
                        con=False
            else:
                while len(c)>1:
                    d=c.copy()
                    c=sub_minus_function(c,ori_b)
                    if c[-1]==0 and len(c)!=1:
                       first_part[0]+=1
                    elif len(c)==1:
                        first_part[0]+=1
                        second_part=np.array([0,0])
                    else:
                        if sign=='-':
                            first_part[0]+=1
                            c[-1]=0
                            second_part=c
                        else:
                            second_part=d   
                        break
        while first_part[-1]==0:
            first_part=np.delete(first_part,-1)
            if len(first_part)==0:
                first_part=np.array([0])
                break
        first_part=np.append(first_part,0)
        return sign+recover_function(first_part)[1:]+recover_function(second_part)
    else:
        return 'impossible'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
def mutlipy_function(ori_a,ori_b,divi=True):
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
                    if c[i+j+k+1]<=9:
                        break
                else: 
                    k+=1
                    if i+j+k==len(ori_a)+len(ori_b)-2:
                        break
    while c[-1]==0 and divi:
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
    n=512
    times=1000
    start=time.time()
    whole_process(n,times)
    end = time.time()
    
    print(n)
    print(times)
    print(end-start)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    