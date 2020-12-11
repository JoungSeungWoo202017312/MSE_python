#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 290 
class 부모:                  # 부모라는 class를 생성
    def __init__(self):      # 자동으로 값을 호출하기 위해 생성자를 사용 (첫 번째 인수를 항상self로 지정해야함)
        print("부모생성")    # "부모생성"을 출력

class 자식(부모):            # 자식class는 부모class에 상속받는다
    def __init__(self):      # 자동으로 값을 호출하기 위해서 생성자를 사용
        print("자식생성")    # '자식생성'을 출력
        super().__init__()   # 부모class를 불러오기 위해 super인자를 사용

나 = 자식()                  # 자식class의 '자식생성을'먼저 출력하고, super로 부모class에 접근하고 init으로 '부모생성'을 출력한다.

