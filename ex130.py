#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 130
import requests     # requests를 삽입해라
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']    # 아 사이트를 가져온 값을 btc라고 한다.

변동폭 = float(btc['max_price']) - float(btc['min_price'])    # 연산을 하기 위해 float를 사용하여 btc의 max_price에서 min_price를 뺀 값은 변동폭
시가 = float(btc['opening_price'])                            # btc의 opening_price를 실수형으로 바꾼 값은 시가
최고가 = float(btc['max_price'])                              # btc의 max_price를 실수형으로 바꾼 값은 최고가

if (시가+변동폭) > 최고가:                                    # 만약 (시가+변동폭)이 최고가 보다 크다면
    print("상승장")                                           # '상승장'을 출력해라
else:                                                         # 그렇지 않다면
    prunt("하락장")                                           # '하락장'을 출력해라

