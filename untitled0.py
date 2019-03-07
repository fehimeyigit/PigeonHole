# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:11:28 2019

@author: FEHİME
"""

import math 
liste =  [1,2,3,4,5,6,7,8,9]
ikililer=[]
#SORU: “S={1,2,3,4,5,6,7,8,9} kümesinin 6 elamanlı her hangi bir altkümesinde toplamı 10 olan iki sayı vardır” ifadesini gösteriniz.
c=0
result=0
for j in liste:
    
    for i in liste:
       result = j+(i)
       if result==10:
         
           print(j,i)
           ikililer.append({j,i})           
       else:
           continue
           
m=len(ikililer)-1
k=0

while(k<m):
    
    if ikililer[k]==ikililer[m]:
    
        k=k+1
        c=c+1
        print(c)
        m=m-1

#Yuva sayısı
#+1  5 den gelen
Grup_sayısı=c+1

#güvercin sayısı
eleman_sayısı=6


en_az= math.ceil(eleman_sayısı/Grup_sayısı)

print(en_az)
