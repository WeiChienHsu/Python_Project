
# coding: utf-8

# Next Prime Number — Have the program find prime numbers until the user chooses to stop asking for the next one.

# In[7]:

def is_prime(num):
    if num == 2:
        return True
    
    for n in range(2,num):
        if num % n == 0:
            return False
    
    return True
    
            


# In[9]:

def next_prime():
    n = 2
    while n:
        if is_prime(n):
            yield (n)
            n +=1
        else:
            n +=1


# In[10]:

def main():
    current_prime = next_prime()
    while True:
        ans = input('do you wanna know the next prime: y/n')
        if ans == 'y':
            print (next(current_prime))

        elif ans =='n':
            print("thanks")
            break

            


# In[ ]:

main()


# Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change

# In[26]:

def money_change(num):
    print ('you get %s quarters'%(int(num/0.25)))
    
    num = num - int(num/0.25)*0.25
    
    print ('you get %s dime'%(int(num/0.1)))
    
    num = num - int(num/0.1)*0.1
    
    print ('you get %s dime'%(int(num/0.05)))
    
    num = num - int(num/0.05)*0.05
    
    print ('you get %s dime'%(int(num/0.01)))
    
    num = num - int(num/0.1)*0.01


# In[29]:

money_change(1.68)


# In[70]:

def money_change_m(num):
    for n in [0.25,0.1,0.05,0.01]:
        yield 'Please give him %s * %s'%(int(num/n),n)
        num = num - (int(num/n))*n


# In[112]:

def check():
    num = float(input('how much you received:'))
    current_change = money_change_m(num)
    n=4
    while n>0:           
        ans = input('tell the machine gonna move on: y/n')
        if ans == 'y':
            print (next(current_change))
            n -= 1


# In[ ]:

check()


# Work out the distance (user specified units) given two cities using haversine equation
# 

# In[1]:

from pygeocoder import Geocoder
import numpy as np
import sys


# In[2]:

def get_latlongs(location):
    return Geocoder.geocode(location)[0].coordinates


# In[4]:

def get_distance(locA, locB): 
    #use haversine forumla(copy from the internet)
    earth_rad = 6371.0
    dlat = np.deg2rad(locB[0] - locA[0])
    dlon = np.deg2rad(locB[1] - locA[1])
    a = np.sin(dlat/2) * np.sin(dlat/2) +         np.cos(np.deg2rad(locA[0])) * np.cos(np.deg2rad(locB[0])) *         np.sin(dlon/2) * np.sin(dlon/2) 
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return earth_rad * c 


# In[5]:

def convert_km_to_miles(km):
    miles_per_km = 0.621371192
    return km * miles_per_km


# In[10]:

-


# In[11]:

count_distance()


# In[ ]:



