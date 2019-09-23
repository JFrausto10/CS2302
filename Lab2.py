# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:04:47 2019

@author: Justus
"""
#########################   Part One   ########################################
def select_bubble(L,k):
    for position in range(len(L)-1,-1,-1):
        for i in range(position):
            if L[i] > L[i+1]:
                temp = L[i+1]
                L[i+1] = L[i]
                L[i] = temp
                return L

def select_quick(L,k):
    smaller=[]
    same=[]
    bigger=[]
    if len(L) >= 1:
        pivot = L[0]
        for i in L:
            if i > pivot:
                bigger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                same.appened(i)
            return select_quick(smaller,k) + same + select_quick(bigger,k) 
    else:
        return L   

def select_modified_quick(L,k):
    smaller=[]
    same=[]
    bigger=[]
    if len(L) > 1:
        pivot = L[0]
        for i in L:
            if i > pivot:
                bigger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                same.append(i)
            if k in smaller:
                return select_modified_quick(smaller,k) 
            elif k in same:
                return select_modified_quick(same,k)
            elif k in bigger:
                return select_modified_quick(bigger,k) 
    else:
        return L


#########################   Part Two   ####################################
'''
def quicksort_stack(l,first,last):
    if first < last:
        p = partition (l,first,last)
        quicksort (l,first, p-1)
        quicksort (l , P+1, last)
        
def modified_quick(L,k):
    smaller=[]
    same=[]
    bigger=[]
    j = len(L)
    while j > 1:
        pivot = L[j]
        for i in L:
            if i > pivot:
                bigger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                same.append(i)
            j-1
    return smaller+same+bigger
'''

#########################   Main Start  ###################################
condition = True
while(condition):
    print("Would you like to focus on part 1 or part 2?")
    print("Enter '1' for part 1")
    print("Enter '2' for part 2")
    print("Enter '3' to exit program")
    userPartChoice = input()
    
    if userPartChoice == '3':
        print("Thank you,havea good day")
        condition = False
        break
        
    print("Enter a series of numbers seperated by commas to serve as a test case")
    testTemp = input()
    testTemp.lower()
    testCase = testTemp.split()
    print("what position would you like to find?")
    userPositionChoice = int(input())
    
    
    if userPartChoice ==  '1':
        conditionPart1 = True
        while(conditionPart1):
            print("What method would you like to use?")
            print("Enter '1' for Bubble Sort")
            print("Enter '2' for Quick Sort")
            print("Enter '3' for Modified Quick Sort")
            print("Enter '4' to go back to part selection")
            print("Enter '5' to exit program")
            userMethodSelection = input()
            
            if userMethodSelection == '1':
                answer = select_bubble(testCase, userPositionChoice)
                print(answer[userPositionChoice])
                
            elif userMethodSelection == '2':
                answer = select_quick(testCase, userPositionChoice)
                print(answer[userPositionChoice])
                
            elif userMethodSelection == '3':
                answer = select_modified_quick(testCase, userPositionChoice)
                print(answer[userPositionChoice])
                
            elif userMethodSelection == '4':
                condidtionPart1 = False
                
            elif userMethodSelection == '5':
                condition = False
                condidtionPart1 = False
                
            else:
                print("That was not a valid choice. please try again.")
                
        
    
    elif userPartChoice == '2':
        conditionPart2 = True
        while(conditionPart2):
            print("What method would you like to use?")
            print("Enter '1' for Quick Sort useing a stack")
            print("Enter '2' for Modified Quick Sort useing only a while loop")
            print("Enter '3' to go back to part selection")
            print("Enter '4' to exit program")
            userMethodSelection = input()
            
            if userMethodSelection == '1':
                conditionPart2 = False
                
            elif userMethodSelection == '2':
                conditionPart2 = False
                
            elif userMethodSelection == '3':
                condidtionPart2 = False
                
            elif userMethodSelection == '4':
                condition = False
                condidtionPart2 = False
                break
                
            else:
                print("That was not a valid choice. please try again.")
        
    else:
        print("That was not a valid choice. please try again.")
