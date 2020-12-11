#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']    # 이 리스트는 date
close_price = [10500, 10300, 10100, 10800, 11000]       # 이 리스트는 close_price
close_table = dict(zip(date, close_price))              # close_table은 date와 close_price를 각각 묶어서 딕셔너리로 변환한 값
print(close_table)                                      # close_table을 출력하라

