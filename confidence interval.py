# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 08:38:23 2024

@author: mahes
"""

import pandas as pd
import numpy as np
from scipy import stats

data = np.random.normal(200, 30, 2000)

mean = np.mean(data)
std = np.std(data)

sample = len(data)
sample
std
mean

import pandas as pd
df = data
df


#==========================================================

from scipy import stats

# 
CI_95 = stats.norm.interval(0.95,loc=200,scale=30)
print("we are 95% confident that, people age is between:",CI_95)

# 
CI_95 = stats.norm.interval(0.99,loc=200,scale=30)
print("we are 99% confident that, people age is between:",CI_95)

# 
CI_95 = stats.norm.interval(0.90,loc=200,scale=30)
print("we are 90% confident that, people age is between:",CI_95)



























    
    