#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 240
def 함수0(num):                # num에 따른 함수, 함수0을 지정
    return num * 2            # 아래에서 받은 num의 값에 num*2를 한다.


def 함수1(num):               # num에 따른 함수, 함수1을 지정
    return 함수0(num + 2)    # 아래에서 받은 num의 값을 num+2를 하여 함수0의 num에 할당한다.

def 함수2(num):              # num의 값에 따른 함수, 함수2를 지정
    num = num +10            # num += 10
    return 함수1(num)        # 함수1의 num에 num+10의 값을 할당.

c = 함수2(2)                 # 함수2의 num에 값에 2를 대입한 값은 c
print(c)                     # c를 출력하라.

