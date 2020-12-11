#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 300
per = ["10.31", "", "8.00"]    # per는 다음과 같은 리스트이다.

for i in per:                  # per의 리스트안의 값들 3개만큼 반복한다.
    try:                       # 실행을한다.
        print(float(i))        # i를 float클래스로 변환한값으로 출력한다.
    except:                    # try에서 예외가 발생했을때
        print(0)               # 0을 출력한다.
    else:                      # try에서 예외가 발생하지 않았을때
        print("clean data")    # 'clean data'를 출력한다.
    finally:                  # try에서 예외가 있던 없던간에 실행한다.
        print("변환 완료")     # '변환 완료'를 출력한다.

