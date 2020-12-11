#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 120
fruit = {"봄":"딸기", "여름":"토마토", "가울":"사과"}    # 이 딕셔너리는 fruit
user = input("좋아하는 과일은?")                         #"좋아하는 과일은?"의 질문에 답을 한다면 그 값은 user
if user in fruit.values():                               # 만약 user가 fruit의 딕셔너리에 존재하는 벨류의 값을 답했다면
    print("정답입니다.")                                 # "정답입니다"를 출력하라
else:                                                    # 그렇지 않다면
    print("오답입니다.")                                 # "오답입니다"를 출력하라

