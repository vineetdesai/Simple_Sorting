# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 11:11:58 2014

@author: Vineet  Desai
"""
myList = list()
myList = [5, 7, 13, 6, 4, 9, 10, 25, 3, 11, 50, 8, 1]
print(str(myList))

counter = 0

#while counter < len(myList):
#    curr = myList[counter]
    
easyList = [3,2,1,4,5]
easyLen = len(easyList)
counter = 0
while counter < easyLen-1:
    if easyList[counter] > easyList[counter+1]:
        temp = easyList[counter]
        easyList[counter] = easyList[counter+1]
        easyList[counter+1] = temp
    counter = counter + 1

print(str(easyList))