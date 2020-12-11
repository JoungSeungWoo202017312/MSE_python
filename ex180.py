#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []                                          # volatility는 [] <--이 리스트이다.
for i in range(len(low_prices)):                         # low_prices의 리스트 안의 갯수만큼 반복하여라
    volatility.append(high_prices[i] - low_prices[i])    # volatility와 high_prices의 리스트에서 low_prices의 리스트를 각각 뺀 값들을 합쳐라
print(volatility)                                        # volatility를 출력하라

