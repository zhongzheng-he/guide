#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:14:31 2020

@author: Zhongzheng
"""

import fabio
import os
 

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   
		os.makedirs(path)            
		print ("---  new folder...  ---")
		print ("---  OK  ---")
 
	else:
		print ("---  There is this folder!  ---")
        
        
here=os.getcwd()+'/'

# =============================================================================
# 02_02 
# =============================================================================
# folder_inspi=here+"/tiff_data/I_fix/"
# folder_expi=here+"/tiff_data/I_mov/"
# folder_PINI=here+"/tiff_data/I_PINI/"
# mkdir(folder_inspi) 
# mkdir(folder_expi)
# mkdir(folder_PINI)





folder1=os.listdir(here)
folder1=folder1[1:6]
print(folder1)
mkdir(here+"tiff_data")

for i in folder1:
    path1=here+i
    folder2=os.listdir(path1)
    folder2=folder2[0+len(folder2)-3:]
    mkdir(here+"tiff_data/"+i)
    print(folder2)
    for j in folder2:
        path2=path1+"/"+j
        mkdir(here+"tiff_data/"+i+"/"+j)
        file=os.listdir(path2)
        
        for k in file:
            image = fabio.open(path2+"/"+k)
            image.convert("tif").save(here+"tiff_data/"+i+"/"+j+"/"+k.replace(".edf",".tif"))
            image.close()
            

            
        
        
    # folder4 = folder3
    # image = fabio.open(here+i)
    # image.convert("tif").save(folder_inspi+i.replace(".edf",".tif"))
    # image.close()
    
    
# file_expi=os.listdir(filePath_expi)
# file_DeltaHU=os.listdir(filePath_DeltaHU)


# for i in file_inspi:
#     image = fabio.open(filePath_inspi+"/"+i)
#     image.convert("tif").save(folder_inspi+i.replace(".edf",".tif"))
#     image.close()
      
      
# for i in file_expi:
#     image = fabio.open(filePath_expi+"/"+i)
#     image.convert("tif").save(folder_expi+i.replace(".edf",".tif"))
    
# for i in file_DeltaHU:
#     image = fabio.open(filePath_DeltaHU+"/"+i)
#     image.convert("tif").save(folder_DeltaHU+i.replace(".edf",".tif"))
#     image.close()
#     image.close()
  
    
# print("08_02  OK!!!!")


# # =============================================================================
# # 06_02 
# # =============================================================================
# folder_inspi=here+"/tiff_data/I_fix/"
# folder_expi=here+"/tiff_data/I_Mov/"
# mkdir(folder_inspi) 
# mkdir(folder_expi)    


# filePath_inspi = './Volumes/1/seg/seg-data/06_02/Seg/M_Inspi'
# filePath_expi = './Volumes/1/seg/seg-data/06_02/Seg/M_Expi'
# file_inspi=os.listdir(filePath_inspi)
# file_expi=os.listdir(filePath_expi)


# for i in file_inspi:
#     image = fabio.open(filePath_inspi+"/"+i)
#     image.convert("tif").save(folder_inspi+i.replace(".edf",".tif"))
#     image.close()
      
      
# for i in file_expi:
#     image = fabio.open(filePath_expi+"/"+i)
#     image.convert("tif").save(folder_expi+i.replace(".edf",".tif"))
#     image.close()
  
    
# print("06_02  OK!!!!")


# # =============================================================================
# # 06_03 
# # =============================================================================
# folder_inspi=here+"/tiff_data/06_03/inspi/"
# folder_expi=here+"/tiff_data/06_03/expi/"
# mkdir(folder_inspi) 
# mkdir(folder_expi)    


# filePath_inspi = '/Volumes/1/seg/seg-data/06_03/Seg/M_Inspi'
# filePath_expi = '/Volumes/1/seg/seg-data/06_03/Seg/M_Expi'
# file_inspi=os.listdir(filePath_inspi)
# file_expi=os.listdir(filePath_expi)


# for i in file_inspi:
#     image = fabio.open(filePath_inspi+"/"+i)
#     image.convert("tif").save(folder_inspi+i.replace(".edf",".tif"))
#     image.close()
      
      
# for i in file_expi:
#     image = fabio.open(filePath_expi+"/"+i)
#     image.convert("tif").save(folder_expi+i.replace(".edf",".tif"))
#     image.close()
  
    
# print("06_03  OK!!!!")