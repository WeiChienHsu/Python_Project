
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
# #### 找出同時存在在各區間的點
# You are responsible for collecting signatures from all tenants of a certain build- ing. For each tenant, you know a period of time when he or she is at home. You would like to collect all signatures by visiting the building as few times as possible.
# The mathematical model for this problem is the following. You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that each segment contains at least one marked point.

# In[272]:

# Uses python3
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    seg_text = segments
    points = []
    inx = 0
    a = 0
    if segments[0][0]==0 and segments[0][1] < segments[1][0]:
        points.append(0)
    if segments[len(segments)-1][0] > segments[len(segments)-2][1]:
        a = segments[len(segments)-1][1]
    
    while len(segments)>1:
        inx = segments[0][1]
        
        if inx > segments[1][0]:
            if inx >= segments[1][1]:
                segments.remove(segments[0])
                continue
            elif inx < segments[1][1]:
                segments.remove(segments[1])
                continue
        
        elif inx < segments[1][0]:
            if segments[0][0] in points:
                segments.remove(segments[0]) 
                continue
            else:
                points.append(inx)
                segments.remove(segments[0])
                continue
        
        elif inx == segments[1][0]:
            if segments[0][0] in points:
                segments.remove(segments[0]) 
                continue
            else:
                points.append(inx)
                segments.remove(segments[0])
                continue
    
    if a:
        points.append(a)
    
    return(points)

    

if __name__ == '__main__':
    put = input()
    n, *data = map(int, put.split())
    segments = sorted(list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2]))))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')


# Input:
# 100
# 41 42
# 52 52
# 63 63
# 80 82
# 78 79
# 35 35
# 22 23
# 31 32
# 44 45
# 81 82
# 36 38
# 10 12
# 1 1
# 23 23
# 32 33
# 87 88
# 55 56
# 69 71
# 89 91
# 93 93
# 38 40
# 33 34
# 14 16
# 57 59
# 70 72
# 36 36
# 29 29
# 73 74
# 66 68
# 36 38
# 1 3
# 49 50
# 68 70
# 26 28
# 30 30
# 1 2
# 64 65
# 57 58
# 58 58
# 51 53
# 41 41
# 17 18
# 45 46
# 4 4
# 0 1
# 65 67
# 92 93
# 84 85
# 75 77
# 39 41
# 15 15
# 29 31
# 83 84
# 12 14
# 91 93
# 83 84
# 81 81
# 3 4
# 66 67
# 8 8
# 17 19
# 86 87
# 44 44
# 34 34
# 74 74
# 94 95
# 79 81
# 29 29
# 60 61
# 58 59
# 62 62
# 54 56
# 58 58
# 79 79
# 89 91
# 40 42
# 2 4
# 12 14
# 5 5
# 28 28
# 35 36
# 7 8
# 82 84
# 49 51
# 2 4
# 57 59
# 25 27
# 52 53
# 48 49
# 9 9
# 10 10
# 78 78
# 26 26
# 83 84
# 22 24
# 86 87
# 52 54
# 49 51
# 63 64
# 54 54
# 

# Output: 1 4 5 8 9 10 14 15 18 23 26 28 29 30 32 34 35 36 40 41 44 46 49 52 54 56 58 61 62 63 65 67 70 74 77 78 79 81 84 87 91 93 95 

# 5 Problem: Maximizing the Number of Prize Places in a Competi- tion

# 
