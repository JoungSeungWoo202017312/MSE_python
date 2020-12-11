#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 160
리스트 = ['intra.h', 'intra.c', 'define.h','run.py']    # 이 list는 리스트이다.
for i in 리스트:                                        # 리스트 안의 갯수만큼 for루프를 돌린다.
    split = i.split(".")                                # i에서 '.'을 기준으로 찢어놓은 값을 split이라고 한다.
    if (split[1] == "h") or (split[1] == "c"):         # split에서 1번째 자리가 h 또는 c 라면
        print(i)                                        # i를 출력해라

