#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0                          # profit은 0
for row in ohlc[1:]:               # ohlc의 전체 리스트의 1번째 자리부터 끝까지를 row에 반복해라
    profit += (row[3] - row[0])    # profit = profit + (row의 3번째 자리들에서 row의 0번째 자리들을 뺀 값)
print(profit)

