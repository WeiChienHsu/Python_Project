
# coding: utf-8

# ## Greedy Algorithm Practice 0823

# ###  1. 加油站問題：從A到B，中間有n個加油站，每次加油後，可跑L公里，請問最少需要加多少次油？
# 
# ####  From the A stop to the B stop, there are n numbers of filling stop located in the middle. After each refilling, the car could run for L miles. To reach the destionation B stop, how many times at least the car need to be refilled?
# 

# In[14]:

x = [0,200,375,550,750,950]
L = 400 #distance with full tank
n = 4 #station

current_loc = 0
number_Refill = 0

while current_loc <= n:
    last_loc = current_loc
    while current_loc <= n and x[current_loc+1]-x[last_loc]<= L:
        current_loc += 1
    
    if x[current_loc] < x[len(x)-1]:
        print('Refill at %s'%(x[current_loc]))
    
    
    if current_loc == last_loc:
        print('impossible')
    
    if current_loc <=n:
        number_Refill += 1

print (number_Refill)


# #### 2.包包問題：一個最大能容納50公斤的包包，現在一共有三樣價值與重量不同的東西要放入其中，請問放置後的最大價值為多少？ 
# 
# ##### A Farctional Knapsack problem: With 50 kg capacity, there's a bag and three different items with differnet weights and values. Try to put the highest values into the bag within the limitation of the bag.

# In[25]:

def find_optinal_value(capacity,values,weights):
    value = 0
    valuePerWeight = sorted([[values/weights,weights] for values,weights in zip(values,weights) ],reverse=True)

    while capacity >0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):        
            if item[1]>0 and item[0]>maxi:
                maxi = item[0]
                idx = i
                
        if idx is None:
            return 0.
        
        w = valuePerWeight[idx][1]
        v_per = valuePerWeight[idx][0]
    
        if w >= capacity:
            value += v_per*capacity
            capacity = 0
            return value
    
        else:
            value += v_per*w
            capacity -= w
    
        valuePerWeight.pop(idx)
            


# In[34]:

capacity = 50
values = [60,100,120]
weights = [20,50,30]


find_optinal_value(capacity,values,weights)


# #### 3.換錢問題：將錢換成10,5,1 output一共需要多少硬幣
# 
# ##### Change the money into coins with coin, penny and cent and output the total amounts.

# In[3]:

num = int(input())
ori_num = num
ans = 0
for n in [10,5,1]:
    ans += int(num/n)
    num = num%n

print("換%s的金額時需要%s個硬幣"%(ori_num,ans))
    


# #### 4.裝包包問題：
# The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines de ne the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.

# In[6]:

def find_optinal_value(capacity,weights,values):
    value = 0
    valuePerWeight = sorted([[values/weights,weights] for values,weights in zip(values,weights) ],reverse=True)

    while capacity >0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):        
            if item[1]>0 and item[0]>maxi:
                maxi = item[0]
                idx = i
                
        if idx is None:  ## 這行不太清楚為什麼要寫，但如果不寫的話壓力測試不會過
            return 0
        
        w = valuePerWeight[idx][1]
        v_per = valuePerWeight[idx][0]
    
        if w >= capacity:
            value += v_per*capacity
            capacity = 0
            return value
    
        else:
            value += v_per*w
            capacity -= w
    
        valuePerWeight.pop(idx)

    return value


# In[7]:

if __name__ == "__main__":
    data = list(map(int,input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = find_optinal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))


# #### 5.從兩數列中找尋相乘最大的解：
# 
# You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up 𝑛 slots on your page and estimated the expected number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

# In[23]:

def max_dot_product(a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res



# In[29]:

if __name__ == '__main__':
    k = input()
    data = list(map(int, k.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))


# #### 6 Problem: Collecting Signatures
# 
# 
# You are responsible for collecting signatures from all tenants of a certain build- ing. For each tenant, you know a period of time when he or she is at home. You would like to collect all signatures by visiting the building as few times as possible.
# The mathematical model for this problem is the following. You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that each segment contains at least one marked point.

# In[ ]:

#待解

