#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 220
def print_max(a, b, c):    # a, b, c의 값에 따른 print_max라는 함수를 지정
    max_val = 0            # max_val는 0
    if a > max_val:        # 만약 a가 max_val보다 크다면
        max_val = a        # max_val는 a의 값
    
    if b > max_val:        # 만약 b가 max_val보다 크다면
        max_val = b        # max_val는 b의 값
        
    if c > max_val:        # 만약 c가 max_val보다 크다면
        max_val = c        # max_val는 c의 값
    print(max_val)         # max_val을 출력하는 것이 print_max의 함수
print_max(2,7,4)

