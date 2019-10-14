# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:05:16 2019

@author: M-Kumar
"""
import cv2

import logical_operations as logic
def encry(img):
    #cv2.imwrite('original.jpg',img)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray.jpg',img)
    height=len(img)
    width=len(img[0])
    key=['1110010110111100111000010100010110011100110111110111000011111110']
    k=0
    flag=1
    for i in range(height):
        for j in range(width):
          if(flag):
               if(k==63):
                  k=0
                  flag=0
               if(key[0][k]):
                  img[i][j]=255-img[i][j]
               else:
                  img[i][j]=0
               k=k+1
          else:
              if(k==63):
                  k=0
                  flag=1
              else:
               cntr=int(len(key[0])/2)
               lindex=cntr-1
               rindex=cntr+1
               while(cntr):
                if(key[0][k]):
                  temp=img[i][lindex]
                  img[i][lindex]=img[i][rindex]
                  img[i][rindex]=temp
                  lindex=lindex-1
                  rindex=rindex+1
                  cntr=cntr-1
                else:
                  img[i][lindex]=0
                  img[i][rindex]=0
                  lindex=lindex-1
                  rindex=rindex+1
                  cntr=cntr-1
              k=k+1

    key8=[]
    a=0
    b=8
    k=0
    for i in range(8):
        key8.append(key[0][a:b])
        a=a+8
        b=b+8
    #print(key8)
    for i in range(height):
        for j in range(width):
            img[i][j]=img[i][j]^int(key8[k],2)
            if(k==7):
                k=0
            else:
                k=k+1
    cv2.imwrite('encrypted.png',img)
##    encrypted=cv2.imread('encrypted.png')
##    cv2.imshow('encrypted',encrypted)
    


    height=len(img)
    width=len(img[0])
    key=['1110010110111100111000010100010110011100110111110111000011111110']
    k=0
    flag=1
    for i in range(height):
        for j in range(width):
          if(flag):
               if(k==63):
                  k=0
                  flag=0
               if(key[0][k]):
                  img[i][j]=255-img[i][j]
               else:
                  img[i][j]=0
               k=k+1
          else:
              if(k==63):
                  k=0
                  flag=1
              else:
               cntr=int(len(key[0])/2)
               lindex=cntr-1
               rindex=cntr+1
               while(cntr):
                if(key[0][k]):
                  temp=img[i][lindex]
                  img[i][lindex]=img[i][rindex]
                  img[i][rindex]=temp
                  lindex=lindex-1
                  rindex=rindex+1
                  cntr=cntr-1
                else:
                  img[i][lindex]=0
                  img[i][rindex]=0
                  lindex=lindex-1
                  rindex=rindex+1
                  cntr=cntr-1
              k=k+1
    key8=[]
    a=0
    b=8
    k=0
    for i in range(8):
        key8.append(key[0][a:b])
        a=a+8
        b=b+8
    for i in range(height):
        for j in range(width):
            img[i][j]=img[i][j]^int(key8[k],2)
            if(k==7):
                k=0
            else:
                k=k+1
    
    #img=cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.imwrite('decrypted.png',img)
##    decrypted=cv2.imread('decrypted.png')
##    cv2.imshow('decrypted.jpg',decrypted)
    

    

